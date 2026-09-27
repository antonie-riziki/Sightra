"""Compatibility entrypoint for Vercel's native Django detection."""

import sys
import importlib.util
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

INNER_WSGI = PROJECT_DIR / "sightra" / "wsgi.py"
spec = importlib.util.spec_from_file_location("sightra_inner_wsgi", INNER_WSGI)
if spec is None or spec.loader is None:
    raise ImportError(f"Unable to load Django WSGI module from {INNER_WSGI}")

inner_wsgi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inner_wsgi)
application = inner_wsgi.application


app = application
