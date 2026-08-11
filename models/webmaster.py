from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from core.database import Base


class Webmaster(Base):
    __tablename__ = "webmasters"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    balance: Mapped[float] = mapped_column(Float, default=0.0)
