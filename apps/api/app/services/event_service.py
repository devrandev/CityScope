from app.models.event import Event
from app.repositories.event_repository import EventRepository


class EventNotFoundError(Exception):
    pass


class EventService:
    def __init__(self, repository: EventRepository):
        self.repository = repository

    def get_all_events(self) -> list[Event]:
        return self.repository.get_all()

    def get_event_by_id(self, event_id: str) -> Event:
        event = self.repository.get_by_id(event_id)

        if event is None:
            raise EventNotFoundError(event_id)

        return event

    def filter_events(
        self,
        district: str | None = None,
        category: str | None = None,
        max_price: int | None = None,
    ) -> list[Event]:
        return self.repository.filter_events(
            district=district,
            category=category,
            max_price=max_price,
        )