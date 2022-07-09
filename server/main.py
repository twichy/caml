import logging
import sys

import uvicorn
from fastapi import FastAPI
# from fastapi_utils.tasks import repeat_every
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import FileResponse
from starlette_exporter import PrometheusMiddleware, handle_metrics

from globals import CONFIG
from middlewares.logger import log_requests
from routes.v1 import v1

# from metrics import test_database_connection


if "pytest" not in sys.modules:
    logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

app = FastAPI()
app.mount("/api/v1", v1)

app.middleware('http')(log_requests)

# Configure prometheus
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

app.mount("/static", StaticFiles(directory="static"), name="static")


# Anything that is not defined above will be redirected to the ui for handling
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return FileResponse('static/index.html')


# @app.on_event("startup")
# @repeat_every(seconds=60 * CONFIG['HEALTH_CHECK_INTERVAL'])  # in minutes
# def perform_health_check() -> None:
#     test_database_connection()


# CORS configurations
origins = ["http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=CONFIG["CAML_DOMAIN"],
        port=int(CONFIG["CAML_PORT"]),
        reload=True
    )
