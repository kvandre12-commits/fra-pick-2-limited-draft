#!/usr/bin/env python3
"""Serve the bundled FRA draft website on localhost."""

from __future__ import annotations

import argparse
import functools
import http.server
import socketserver
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent


class LocalServer(socketserver.ThreadingTCPServer):
    """Small reusable localhost server for the static app."""

    allow_reuse_address = True
    daemon_threads = True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8780, help="localhost port")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not 1024 <= args.port <= 65535:
        raise SystemExit("--port must be between 1024 and 65535")

    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler,
        directory=str(SKILL_DIR),
    )
    with LocalServer(("127.0.0.1", args.port), handler) as server:
        print(f"FRA Pick 2 Limited Draft: http://127.0.0.1:{args.port}/", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
