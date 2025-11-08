from datetime import datetime

from sqlalchemy import DateTime, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

from src.settings import APP_LINK_TTL_DAYS


Base = declarative_base()


class ShortLinkModel(Base):
    __tablename__ = 'short-links'

    id: Mapped[str] = mapped_column(primary_key=True)
    original_link: Mapped[str]
    ends_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text(f"CURRENT_TIMESTAMP + interval '{APP_LINK_TTL_DAYS} days'"),
    )
