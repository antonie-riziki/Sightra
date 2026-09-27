"""Compatibility entrypoint for Vercel's native Django detection."""

import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from sightra.wsgi import application  # noqa: E402


app = application
