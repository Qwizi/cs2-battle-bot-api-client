from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.map_sides_enum import MapSidesEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_config_cvars import MatchConfigCvars
    from ..models.match_config_team_1 import MatchConfigTeam1
    from ..models.match_config_team_2 import MatchConfigTeam2


T = TypeVar("T", bound="MatchConfig")


@_attrs_define
class MatchConfig:
    """
    Attributes:
        matchid (str):
        team1 (MatchConfigTeam1):
        team2 (MatchConfigTeam2):
        num_maps (int):
        maplist (List[str]):
        map_sides (List[MapSidesEnum]):
        clinch_series (bool):
        players_per_team (int):
        cvars (Union[Unset, MatchConfigCvars]):
    """

    matchid: str
    team1: "MatchConfigTeam1"
    team2: "MatchConfigTeam2"
    num_maps: int
    maplist: List[str]
    map_sides: List[MapSidesEnum]
    clinch_series: bool
    players_per_team: int
    cvars: Union[Unset, "MatchConfigCvars"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        matchid = self.matchid

        team1 = self.team1.to_dict()

        team2 = self.team2.to_dict()

        num_maps = self.num_maps

        maplist = self.maplist

        map_sides = []
        for map_sides_item_data in self.map_sides:
            map_sides_item = map_sides_item_data.value
            map_sides.append(map_sides_item)

        clinch_series = self.clinch_series

        players_per_team = self.players_per_team

        cvars: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cvars, Unset):
            cvars = self.cvars.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matchid": matchid,
                "team1": team1,
                "team2": team2,
                "num_maps": num_maps,
                "maplist": maplist,
                "map_sides": map_sides,
                "clinch_series": clinch_series,
                "players_per_team": players_per_team,
            }
        )
        if cvars is not UNSET:
            field_dict["cvars"] = cvars

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.match_config_cvars import MatchConfigCvars
        from ..models.match_config_team_1 import MatchConfigTeam1
        from ..models.match_config_team_2 import MatchConfigTeam2

        d = src_dict.copy()
        matchid = d.pop("matchid")

        team1 = MatchConfigTeam1.from_dict(d.pop("team1"))

        team2 = MatchConfigTeam2.from_dict(d.pop("team2"))

        num_maps = d.pop("num_maps")

        maplist = cast(List[str], d.pop("maplist"))

        map_sides = []
        _map_sides = d.pop("map_sides")
        for map_sides_item_data in _map_sides:
            map_sides_item = MapSidesEnum(map_sides_item_data)

            map_sides.append(map_sides_item)

        clinch_series = d.pop("clinch_series")

        players_per_team = d.pop("players_per_team")

        _cvars = d.pop("cvars", UNSET)
        cvars: Union[Unset, MatchConfigCvars]
        if isinstance(_cvars, Unset):
            cvars = UNSET
        else:
            cvars = MatchConfigCvars.from_dict(_cvars)

        match_config = cls(
            matchid=matchid,
            team1=team1,
            team2=team2,
            num_maps=num_maps,
            maplist=maplist,
            map_sides=map_sides,
            clinch_series=clinch_series,
            players_per_team=players_per_team,
            cvars=cvars,
        )

        match_config.additional_properties = d
        return match_config

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
