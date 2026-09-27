from pathlib import Path

from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render

def dashboard(request):
    return render(request, "dashboard.html")

def landing_page(request):
    return render(request, "landing-page.html")


def service_worker(request):
    """Serve the PWA worker from the site root so it can control all routes."""
    worker_path = Path(settings.BASE_DIR) / "static" / "sightra" / "service-worker.js"
    response = FileResponse(worker_path.open("rb"), content_type="application/javascript")
    response["Service-Worker-Allowed"] = "/"
    response["Cache-Control"] = "no-cache"
    return response
