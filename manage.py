#!/usr/bin/env python
"""Repository-level Django entrypoint for Vercel and local tooling."""

import os
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent / "sightra"
sys.path.insert(0, str(PROJECT_DIR))


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sightra.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
