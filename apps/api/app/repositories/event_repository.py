import json
from pathlib import Path

from app.models.event import Event


class EventRepository:
    def __init__(self) -> None:
        self.file_path = Path("data/events.json")

    def get_all(self) -> list[Event]:
        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return [Event(**item) for item in data]

    def get_by_id(self, event_id: str) -> Event | None:
        for event in self.get_all():
            if event.id == event_id:
                return event

        return None

    def filter_events(
        self,
        district: str | None = None,
        category: str | None = None,
        max_price: int | None = None,
    ) -> list[Event]:
        events = self.get_all()

        if district:
            events = [
                event for event in events
                if event.district.lower() == district.lower()
            ]

        if category:
            events = [
                event for event in events
                if event.category.lower() == category.lower()
            ]

        if max_price is not None:
            events = [
                event for event in events
                if event.price <= max_price
            ]

        return events