from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, List






T = TypeVar("T", bound="MatchBanMapResult")


@_attrs_define
class MatchBanMapResult:
    """ 
        Attributes:
            banned_map (str):
            next_ban_team_leader (str):
            maps_left (List[str]):
            map_bans_count (int):
     """

    banned_map: str
    next_ban_team_leader: str
    maps_left: List[str]
    map_bans_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        banned_map = self.banned_map

        next_ban_team_leader = self.next_ban_team_leader

        maps_left = self.maps_left





        map_bans_count = self.map_bans_count


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "banned_map": banned_map,
            "next_ban_team_leader": next_ban_team_leader,
            "maps_left": maps_left,
            "map_bans_count": map_bans_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        banned_map = d.pop("banned_map")

        next_ban_team_leader = d.pop("next_ban_team_leader")

        maps_left = cast(List[str], d.pop("maps_left"))


        map_bans_count = d.pop("map_bans_count")

        match_ban_map_result = cls(
            banned_map=banned_map,
            next_ban_team_leader=next_ban_team_leader,
            maps_left=maps_left,
            map_bans_count=map_bans_count,
        )

        match_ban_map_result.additional_properties = d
        return match_ban_map_result

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
