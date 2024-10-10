from pydantic import BaseModel
from typing import List

class StyleRequest(BaseModel):
    event_type: str
    user_preferences: List[str] = None

class StyleResponse(BaseModel):
    event_type: str
    suggested_style: str

class LayoutRequest(BaseModel):
    event_type: str
    room_size: int = None

class LayoutResponse(BaseModel):
    event_type: str
    suggested_layout: str
