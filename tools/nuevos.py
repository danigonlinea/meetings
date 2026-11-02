#!/usr/bin/env python3
"""Lista lo que aún no está ingerido, sin descargar nada.

Uso:
    python3 tools/nuevos.py              # canal + webinars
    python3 tools/nuevos.py --canal 10   # mira 10 vídeos del canal
    python3 tools/nuevos.py --json       # salida para el agente

El canal se identifica por ID (`UCEXbEm8RUvRkKUEo2RjKd9w`, «La Pizarra de Andrés»),
no por handle: `@LaPizarradeAndrésLive` es OTRO canal y no es el que se ingiere.

Solo compara `source.video_id`, nunca títulos: `yt-dlp --flat-playlist` devuelve los
títulos traducidos al inglés y el slug saldría mal.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHANNEL_ID = "UCEXbEm8RUvRkKUEo2RjKd9w"
CHANNEL_URL = f"https://www.youtube.com/channel/{CHANNEL_ID}"


def ingested() -> set[str]:
    ids = set()
    for path in ROOT.glob("*/*/*/transcript.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        video_id = data.get("source", {}).get("video_id")
        if video_id:
            ids.add(video_id)
    return ids


def channel_ids(limit: int) -> list[str]:
    try:
        result = subprocess.run(
            [
                "yt-dlp",
                "--flat-playlist",
                "--playlist-end",
                str(limit),
                "--print",
                "%(id)s",
                f"{CHANNEL_URL}/videos",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        sys.exit("yt-dlp no está instalado")
    if result.returncode != 0:
        sys.exit(f"yt-dlp falló: {result.stderr.strip().splitlines()[-1] if result.stderr else 'sin detalle'}")
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def webinars_pending() -> list[str]:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "myinvestor_webinars.py"), "pendientes"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--canal", type=int, default=10, help="vídeos a mirar del canal")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    known = ingested()
    new = [v for v in channel_ids(args.canal) if v not in known]
    pending = webinars_pending()

    if args.json:
        print(
            json.dumps(
                {
                    "canal_id": CHANNEL_ID,
                    "videos_nuevos": [{"id": v, "url": f"https://www.youtube.com/watch?v={v}"} for v in new],
                    "webinars_pendientes": len(pending),
                    "webinars": [line.split("\t")[0] for line in pending],
                },
                ensure_ascii=False,
                indent=1,
            )
        )
        return 0

    print(f"Canal {CHANNEL_ID}: {len(new)} vídeos nuevos de los {args.canal} últimos")
    for video_id in new:
        print(f"  https://www.youtube.com/watch?v={video_id}")
    print(f"Webinars MyInvestor pendientes: {len(pending)}")
    for line in pending[:5]:
        print(f"  {line}")
    if not new and not pending:
        print("\nNada que ingerir.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
