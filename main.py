from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.database import engine, Base
from models import Webmaster, Offer, Conversion
from api.tds import router as tds_router
from api.postback import router as postback_router
from api.offers import router as offer_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for application startup and shutdown events.
    Replaces the deprecated @app.on_event("startup").
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(
    title="Highload Affiliate Tracking API",
    description="TDS and Postback processing microservice",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(tds_router)
app.include_router(postback_router)
app.include_router(offer_router)


@app.get("/health", tags=["System"])
async def health_check():
    """Basic endpoint to check the health status of the service"""
    return {"status": "ok", "message": "Service is running!"}
