from dataclasses import dataclass
from typing import List, Optional

@dataclass
class TravelRequest:
    destination: str
    days: int

    def __post_init__(self):
        if not self.destination or len(self.destination) < 1:
            raise ValueError("Destination must not be empty")
        if self.days <= 0:
            raise ValueError("Days must be greater than 0")

@dataclass
class Itinerary:
    destination: str
    days: int
    daily_plans: List[str]

@dataclass
class ItineraryResponse:
    destination: str
    itinerary: List[str]
    total_days: int
    recommendations: Optional[List[str]] = None