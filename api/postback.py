from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import redis.asyncio as redis
from core.config import settings
from workers.tasks import process_conversion

router = APIRouter(tags=["Postback Processing"])
redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, decode_responses=True)


class PostbackData(BaseModel):
    click_id: str
    payout: float


@router.post("/s2s/postback")
async def receive_postback(postback: PostbackData):
    click_data = await redis_client.hgetall(postback.click_id)

    if not click_data:
        raise HTTPException(status_code=404, detail="Click ID not found in cache")

    webmaster_id = int(click_data["webmaster_id"])
    offer_id = int(click_data["offer_id"])
    process_conversion.delay(
        click_id=postback.click_id,
        webmaster_id=webmaster_id,
        offer_id=offer_id,
        payout=postback.payout
    )

    return {"status": "accepted_for_processing"}
