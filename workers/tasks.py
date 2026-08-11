import asyncio
from workers.celery_app import celery_app
from core.database import async_session_maker
from models import Conversion, Webmaster


async def async_save_conversion(click_id: str, webmaster_id: int, offer_id: int, payout: float):
    """Async function to perform database operations"""
    async with async_session_maker() as session:
        new_conversion = Conversion(
            click_id=click_id,
            webmaster_id=webmaster_id,
            offer_id=offer_id,
            payout=payout
        )
        session.add(new_conversion)

        webmaster = await session.get(Webmaster, webmaster_id)
        if webmaster:
            webmaster.balance += payout

        await session.commit()


@celery_app.task
def process_conversion(click_id: str, webmaster_id: int, offer_id: int, payout: float):
    """
    Celery task that picks up the job from Redis
    and runs the async DB logic.
    """
    asyncio.run(async_save_conversion(click_id, webmaster_id, offer_id, payout))
