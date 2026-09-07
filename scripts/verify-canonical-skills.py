#!/usr/bin/env python3
"""Verify vendored skills against the pinned canonical release hashes."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins" / "customer-identity" / "skills"
SOURCE = SKILLS / "SOURCE.json"


def main() -> None:
    metadata = json.loads(SOURCE.read_text(encoding="utf-8"))
    if metadata.get("repository") != "https://github.com/namoidhq/namoid-agent-integrations":
        raise SystemExit("unexpected canonical repository")
    if not str(metadata.get("tag", "")).startswith("v"):
        raise SystemExit("canonical source must use an immutable version tag")

    for relative, expected in metadata["files"].items():
        target = SKILLS / relative
        if not target.is_file() or target.is_symlink():
            raise SystemExit(f"missing or unsafe canonical skill file: {relative}")
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != expected:
            raise SystemExit(f"canonical skill drift: {relative}")

    print(f"Verified {len(metadata['files'])} canonical skill files from {metadata['tag']}.")


if __name__ == "__main__":
    main()

