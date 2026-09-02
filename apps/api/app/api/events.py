from fastapi import APIRouter, HTTPException, Query

from app.models.event import Event
from app.repositories.event_repository import EventRepository
from app.services.event_service import EventNotFoundError, EventService


router = APIRouter(
    prefix="/api/v1/events",
    tags=["events"],
)

repository = EventRepository()
service = EventService(repository)



@router.get("", response_model=list[Event])
def get_events(
    district: str | None = None,
    category: str | None = None,
    max_price: int | None = Query(default=None, ge=0),
):
    return service.filter_events(
        district=district,
        category=category,
        max_price=max_price,
    )


@router.get("/{event_id}", response_model=Event)
def get_event(event_id: str):
    try:
        return service.get_event_by_id(event_id)
    except EventNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Event not found",
        )