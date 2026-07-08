from fastapi import FastAPI

from backend.core.config import APP_NAME

from backend.core.logger import logger

from backend.api.routes.upload import router as upload_router
from backend.api.routes.search import router as search_router
from backend.api.routes.chat import router as chat_router
from backend.database.init_db import initialize_database


app = FastAPI(

    title=APP_NAME,

    version="3.0.0",

    description="Production AI Research Assistant"

)

initialize_database()

# --------------------------------------------------

app.include_router(upload_router)

app.include_router(search_router)

app.include_router(chat_router)

# --------------------------------------------------


@app.get("/")

def root():

    logger.info("Health endpoint called.")

    return {

        "application": APP_NAME,

        "status": "running",

        "version": "3.0.0"

    }


@app.get("/health")

def health():

    return {

        "status": "healthy"

    }