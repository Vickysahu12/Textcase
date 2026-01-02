from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, DateTime
from datetime import datetime, timezone
from app.db.config import Base

class UserCredits(Base):
    __tablename__ = "user_credits"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), unique=True)
    credits: Mapped[int] = mapped_column(Integer, default=10)