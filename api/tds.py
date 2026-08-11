import uuid
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
import redis.asyncio as redis
from sqlalchemy.ext.asyncio import AsyncSession
from core.config import settings
from core.database import get_db
from models import Offer

router = APIRouter(tags=["TDS - Traffic Delivery System"])
redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, decode_responses=True)


@router.get("/click")
async def handle_click(offer_id: int, webmaster_id: int, db: AsyncSession = Depends(get_db)):
    click_id = f"click_{uuid.uuid4().hex}"

    offer = await db.get(Offer, offer_id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")

    await redis_client.hset(
        name=click_id,
        mapping={"webmaster_id": webmaster_id, "offer_id": offer_id}
    )
    await redis_client.expire(name=click_id, time=86400)

    advertiser_url = offer.advertiser_url.replace("{click_id}", click_id)

    return RedirectResponse(url=advertiser_url, status_code=307)
