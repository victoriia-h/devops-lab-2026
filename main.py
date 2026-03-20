import sys
import logging
import subprocess
from contextlib import asynccontextmanager
from fastapi import FastAPI, Response, status
from pythonjsonlogger import jsonlogger
from database import check_db_connection, engine

# Configure JSON logging for ELK/Prometheus
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logHandler = logging.StreamHandler(sys.stdout)
formatter = jsonlogger.JsonFormatter(
    '%(asctime)s %(levelname)s %(message)s', 
    rename_fields={"asctime": "timestamp", "levelname": "level"}
)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application is starting up...")
    logger.info("Running database migrations...")
    try:
        # Automated migration execution on startup
        subprocess.run(["alembic", "upgrade", "head"], check=True, capture_output=True)
        logger.info("Migrations applied successfully.")
    except Exception as e:
        logger.warning(f"Migrations step skipped: {e}")
        
    yield
    logger.info("SIGTERM received. Starting graceful shutdown...")
    engine.dispose()
    logger.info("Graceful shutdown completed. Exiting with code 0.")

app = FastAPI(lifespan=lifespan)

@app.get("/health")
async def health_check(response: Response):
    logger.info("Health check requested")
    if check_db_connection():
        return {"status": "ok", "database": "connected"}
    else:
        logger.error("DB connection failed")
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "error", "database": "disconnected"}