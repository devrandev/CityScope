from pydantic import BaseModel

class Event(BaseModel):
    id: str
    title: str
    description: str
    category: str
    district: str
    price: int