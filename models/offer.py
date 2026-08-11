from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from core.database import Base


class Offer(Base):
    __tablename__ = "offers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    advertiser_url: Mapped[str] = mapped_column(String(500))
    payout: Mapped[float] = mapped_column(Float)
