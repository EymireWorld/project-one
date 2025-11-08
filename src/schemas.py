from datetime import datetime

from pydantic import BaseModel, HttpUrl


class ShortLinkSchema(BaseModel):
    id: str
    original_link: HttpUrl
    ends_at: datetime


class ShortLinkAddSchema(BaseModel):
    original_url: HttpUrl


class ShortLinkShowSchema(BaseModel):
    short_url: HttpUrl
