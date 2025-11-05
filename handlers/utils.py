from aiogram.filters.callback_data import CallbackData
from typing import Optional

class FindCallback(CallbackData, prefix="find"):
    action: str
    id: Optional[int] = None
    content_type: Optional[str] = None
    title: Optional[str] = None
    lang: Optional[str] = None

