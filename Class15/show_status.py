from enum import Enum

MAX_TICKETS_PER_BOOKING = 60


class ShowStatus(Enum):
    OPEN = "Open"
    CANCELLED = "Cancelled"
    SOLD_OUT = "Sold Out"
