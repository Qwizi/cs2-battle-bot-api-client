from enum import Enum

class StatusEnum(str, Enum):
    CREATED = "CREATED"
    FINISHED = "FINISHED"
    LIVE = "LIVE"
    STARTED = "STARTED"

    def __str__(self) -> str:
        return str(self.value)
