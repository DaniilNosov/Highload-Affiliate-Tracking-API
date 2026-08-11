from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import async_session_maker
from models import Offer

router = APIRouter(tags=["Admin - Offers"], prefix="/admin/offers")


async def get_db():
    async with async_session_maker() as session:
        yield session


class OfferCreate(BaseModel):
    name: str
    advertiser_url: str
    payout: float


@router.post("/")
async def create_offer(offer: OfferCreate, db: AsyncSession = Depends(get_db)):
    """making new offer"""
    new_offer = Offer(
        name=offer.name,
        advertiser_url=offer.advertiser_url,
        payout=offer.payout
    )
    db.add(new_offer)
    await db.commit()
    await db.refresh(new_offer)

    return {"status": "success", "offer_id": new_offer.id}


@router.get("/")
async def get_offers(db: AsyncSession = Depends(get_db)):
    """Get all offers"""
    result = await db.execute(select(Offer))
    return result.scalars().all()
