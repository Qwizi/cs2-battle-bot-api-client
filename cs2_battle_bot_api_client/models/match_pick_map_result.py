from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.map_ import Map
    from ..models.team import Team


T = TypeVar("T", bound="MatchPickMapResult")


@_attrs_define
class MatchPickMapResult:
    """
    Attributes:
        picked_map (Map):
        next_pick_team (Team):
        maps_left (List[str]):
        map_picks_count (int):
    """

    picked_map: "Map"
    next_pick_team: "Team"
    maps_left: List[str]
    map_picks_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        picked_map = self.picked_map.to_dict()

        next_pick_team = self.next_pick_team.to_dict()

        maps_left = self.maps_left

        map_picks_count = self.map_picks_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "picked_map": picked_map,
                "next_pick_team": next_pick_team,
                "maps_left": maps_left,
                "map_picks_count": map_picks_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_ import Map
        from ..models.team import Team

        d = src_dict.copy()
        picked_map = Map.from_dict(d.pop("picked_map"))

        next_pick_team = Team.from_dict(d.pop("next_pick_team"))

        maps_left = cast(List[str], d.pop("maps_left"))

        map_picks_count = d.pop("map_picks_count")

        match_pick_map_result = cls(
            picked_map=picked_map,
            next_pick_team=next_pick_team,
            maps_left=maps_left,
            map_picks_count=map_picks_count,
        )

        match_pick_map_result.additional_properties = d
        return match_pick_map_result

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
