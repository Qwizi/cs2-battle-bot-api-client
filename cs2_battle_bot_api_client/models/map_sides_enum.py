from enum import Enum


class MapSidesEnum(str, Enum):
    KNIFE = "knife"
    TEAM1_CT = "team1_ct"
    TEAM1_T = "team1_t"
    TEAM2_CT = "team2_ct"
    TEAM2_T = "team2_t"

    def __str__(self) -> str:
        return str(self.value)
