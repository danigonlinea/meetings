#!/usr/bin/env python3
"""Cliente del MCP público de MyInvestor (streamable HTTP + SSE).

No hace falta instalar nada: `mcp.myinvestor.es` es público y no pide credenciales.
Devuelve las fichas del catálogo (2.400+ fondos) con TER, `distributing`, allocations,
mínimos, cortes, geografía, sectores y series de precio; y permite backtest de carteras.

Uso:
    python3 tools/myinvestor_mcp.py tools
    python3 tools/myinvestor_mcp.py buscar "vanguard small-cap" --limit 5
    python3 tools/myinvestor_mcp.py buscar "indexado" --asset-type "Renta Variable" --max-ter 0.2
    python3 tools/myinvestor_mcp.py ficha IE00B03HD191 IE0031786696
    python3 tools/myinvestor_mcp.py facetas management_company --top 20
    python3 tools/myinvestor_mcp.py backtest 65:IE000ZYRH0Q7 10:IE000QAZP7L2 10:IE00B42W4L06
    python3 tools/myinvestor_mcp.py llamar get_funds '{"isins":["IE00B03HD191"]}'

Las herramientas con vista (`search_funds`, `backtest_portfolio`) devuelven el resumen en
texto y los datos en `structuredContent`; `--json` imprime el JSON completo.
"""

from __future__ import annotations

import json
import sys

import requests

URL = "https://mcp.myinvestor.es/mcp"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
}


class MCP:
    """Sesión MCP mínima: initialize, tools/list y tools/call sobre SSE."""

    def __init__(self, url: str = URL) -> None:
        self.url = url
        self.session = requests.Session()
        self.session_id: str | None = None
        self._id = 0

    def _headers(self) -> dict[str, str]:
        headers = dict(HEADERS)
        if self.session_id:
            headers["Mcp-Session-Id"] = self.session_id
        return headers

    def _post(self, payload: dict):
        response = self.session.post(
            self.url, headers=self._headers(), json=payload, timeout=180, stream=True
        )
        session_id = response.headers.get("Mcp-Session-Id") or response.headers.get(
            "mcp-session-id"
        )
        if session_id:
            self.session_id = session_id
        return response

    @staticmethod
    def _read_sse(response, want_id: int) -> dict | None:
        # SSE sin charset: requests decodifica como latin-1 y rompe los acentos.
        # Se leen bytes y se decodifican como UTF-8 explícitamente.
        for raw_bytes in response.iter_lines():
            if not raw_bytes:
                continue
            raw = raw_bytes.decode("utf-8", errors="replace")
            if not raw.strip().startswith("data:"):
                continue
            try:
                message = json.loads(raw.split(":", 1)[1].strip())
            except json.JSONDecodeError:
                continue
            if message.get("id") == want_id:
                return message
        return None

    def call(self, method: str, params: dict | None = None, notify: bool = False) -> dict | None:
        self._id += 1
        payload: dict = {"jsonrpc": "2.0", "method": method}
        if params is not None:
            payload["params"] = params
        if not notify:
            payload["id"] = self._id
        response = self._post(payload)
        if notify:
            return None
        if response.headers.get("content-type", "").startswith("application/json"):
            return json.loads(response.content.decode("utf-8"))
        return self._read_sse(response, self._id)

    def init(self) -> dict:
        out = self.call(
            "initialize",
            {
                "protocolVersion": "2025-06-18",
                "capabilities": {},
                "clientInfo": {"name": "meetings-repo", "version": "1.0"},
            },
        )
        self.call("notifications/initialized", {}, notify=True)
        return out or {}

    def tools(self) -> dict:
        return self.call("tools/list", {}) or {}

    def tool(self, name: str, arguments: dict) -> dict:
        return self.call("tools/call", {"name": name, "arguments": arguments}) or {}


def resumen(resultado: dict) -> str:
    """Texto que devuelve el servidor (resumen legible de la vista)."""
    if not resultado or "result" not in resultado:
        return json.dumps(resultado, ensure_ascii=False)[:2000]
    partes = [
        bloque["text"]
        for bloque in resultado["result"].get("content", [])
        if bloque.get("type") == "text"
    ]
    return "\n".join(partes)


def datos(resultado: dict) -> dict:
    return (resultado.get("result") or {}).get("structuredContent") or {}


def contenido(resultado: dict) -> dict:
    """Cuerpo útil: `structuredContent.data` (fondos, backtest, facetas)."""
    return datos(resultado).get("data") or {}


def main(argv: list[str]) -> int:
    if not argv or argv[0] in {"-h", "--help"}:
        print(__doc__)
        return 0

    mcp = MCP()
    mcp.init()
    orden, resto, flags = argv[0], [], set()
    for arg in argv[1:]:
        if arg == "--json":
            flags.add("json")
        else:
            resto.append(arg)

    def opcion(nombre: str, defecto=None):
        if nombre in resto:
            return resto[resto.index(nombre) + 1]
        return defecto

    if orden == "tools":
        for herramienta in mcp.tools()["result"]["tools"]:
            print(
                f"{herramienta['name']}: "
                f"{(herramienta.get('description') or '').splitlines()[0][:150]}"
            )
        return 0

    if orden == "buscar":
        args: dict = {"limit": int(opcion("--limit") or 10)}
        if resto and not resto[0].startswith("--"):
            args["query"] = resto[0]
        for valor, clave in (
            ("--asset-type", "asset_type"),
            ("--geography", "geography"),
            ("--sector", "sector"),
            ("--management-type", "management_type"),
            ("--order-by", "order_by"),
        ):
            if opcion(valor):
                args[clave] = opcion(valor)
        if opcion("--max-ter"):
            args["max_ter"] = float(opcion("--max-ter") or 0)
        resultado = mcp.tool("search_funds", args)
        print(resumen(resultado))
        if "json" in flags:
            print(json.dumps(datos(resultado), ensure_ascii=False, indent=1))
        return 0

    if orden == "ficha":
        if not resto:
            print("faltan ISIN", file=sys.stderr)
            return 2
        resultado = mcp.tool("get_funds", {"isins": resto})
        if "json" in flags:
            print(json.dumps(datos(resultado), ensure_ascii=False, indent=1))
            return 0
        fichas = contenido(resultado).get("funds", [])
        if not fichas:
            print("sin datos: el catálogo no devuelve ficha para esos ISIN")
        for ficha in fichas:
            print(f"{ficha['isin']} | {ficha['name']}")
            print(
                f"  TER {ficha['ter']} | distribuyendo {ficha['distributing']} | "
                f"{ficha['management_type']} | riesgo {ficha['risk_indicator']} | {ficha['currency']}"
            )
            print(
                f"  RV {ficha['alloc_equity']} | RF {ficha['alloc_bond']} | "
                f"caja {ficha['alloc_cash']} | otros {ficha['alloc_other']}"
            )
            print(
                f"  mínimo {ficha['min_initial']} | corte {ficha['cutoff_time']} | "
                f"suscripción {ficha['subscription_lag_days']}d | reembolso {ficha['redemption_lag_days']}d"
            )
            if ficha.get("warning_text"):
                print(f"  ⚠️  {ficha['warning_text']}")
        faltan = contenido(resultado).get("missing") or []
        if faltan:
            print("no encontrados:", ", ".join(faltan))
        return 0

    if orden == "facetas":
        dimensiones = [resto[0]] if resto else None
        args = {"top": int(opcion("--top") or 50)}
        if dimensiones:
            args["dimensions"] = dimensiones
        print(resumen(mcp.tool("list_facets", args)))
        return 0

    if orden == "backtest":
        holdings = []
        for token in resto:
            if ":" not in token:
                continue
            peso, ref = token.split(":", 1)
            holdings.append({"ref": ref, "weight_pct": float(peso)})
        if not holdings:
            print("usa <peso>:<ISIN/ticker> ...", file=sys.stderr)
            return 2
        resultado = mcp.tool("backtest_portfolio", {"holdings": holdings})
        print(resumen(resultado))
        return 0

    if orden == "llamar":
        if len(resto) < 2:
            print("uso: llamar <herramienta> '<json>'", file=sys.stderr)
            return 2
        resultado = mcp.tool(resto[0], json.loads(resto[1]))
        print(resumen(resultado))
        if "json" in flags:
            print(json.dumps(datos(resultado), ensure_ascii=False, indent=1))
        return 0

    print(f"orden desconocida: {orden}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
