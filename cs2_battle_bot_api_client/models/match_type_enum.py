from enum import Enum

class MatchTypeEnum(str, Enum):
    BO1 = "BO1"
    BO3 = "BO3"
    BO5 = "BO5"

    def __str__(self) -> str:
        return str(self.value)
