from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Integer
from core.database import Base


class Conversion(Base):
    __tablename__ = "conversions"

    id: Mapped[int] = mapped_column(primary_key=True)
    click_id: Mapped[str] = mapped_column(String(100), unique=True)
    webmaster_id: Mapped[int] = mapped_column(Integer)
    offer_id: Mapped[int] = mapped_column(Integer)
    payout: Mapped[float] = mapped_column(Float)
