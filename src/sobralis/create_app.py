import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sobralis import router
from sobralis.db.connection import pool

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await pool.open()
    await pool.wait()
    logger.info("Application started")

    try:
        yield
    finally:
        logger.info("Shutting down")
        await pool.close()


def create_app() -> FastAPI:
    app = FastAPI(
        title="Собрались",
        lifespan=lifespan,
    )

    app.include_router(router)

    return app
