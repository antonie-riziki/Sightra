"""Vercel entrypoint for the existing Django application.

The repository keeps the Django project in ``sightra/`` while Vercel's
project root is the repository root. Add that directory to the import path
before loading the unchanged Django WSGI application.
"""

import os
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1] / "sightra"
sys.path.insert(0, str(PROJECT_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sightra.settings")

from django.core.wsgi import get_wsgi_application  # noqa: E402


app = get_wsgi_application()
application = app
