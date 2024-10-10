from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
from utils import suggest_style_openai, suggest_layout_openai
from schemas import StyleRequest, StyleResponse, LayoutRequest, LayoutResponse

router = APIRouter()

@router.post("/suggest_style", response_model=StyleResponse)
def get_style_suggestion(style_request: StyleRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    event_type = style_request.event_type
    user_preferences = style_request.user_preferences
    suggested_style = suggest_style_openai(event_type, user_preferences)
    return {"event_type": event_type, "suggested_style": suggested_style}

@router.post("/suggest_layout", response_model=LayoutResponse)
def get_layout_suggestion(layout_request: LayoutRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    event_type = layout_request.event_type
    room_size = layout_request.room_size
    suggested_layout = suggest_layout_openai(event_type, room_size)
    return {"event_type": event_type, "suggested_layout": suggested_layout}
