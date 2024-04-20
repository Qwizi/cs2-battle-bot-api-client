from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.map_sides_enum import MapSidesEnum
from ..models.status_enum import StatusEnum
from ..models.type_enum import TypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_update_cvars import MatchUpdateCvars


T = TypeVar("T", bound="MatchUpdate")


@_attrs_define
class MatchUpdate:
    """
    Attributes:
        status (Union[Unset, StatusEnum]): * `CREATED` - Created
            * `STARTED` - Started
            * `LIVE` - Live
            * `FINISHED` - Finished
        type (Union[Unset, TypeEnum]): * `BO1` - Bo1
            * `BO3` - Bo3
            * `BO5` - Bo5
        team1_id (Union[Unset, str]):
        team2_id (Union[Unset, str]):
        map_sides (Union[Unset, List[MapSidesEnum]]):
        clinch_series (Union[Unset, bool]):
        cvars (Union[Unset, MatchUpdateCvars]):
        message_id (Union[Unset, str]):
        author_id (Union[Unset, str]):
        server_id (Union[Unset, str]):
        guild_id (Union[Unset, str]):
    """

    status: Union[Unset, StatusEnum] = UNSET
    type: Union[Unset, TypeEnum] = UNSET
    team1_id: Union[Unset, str] = UNSET
    team2_id: Union[Unset, str] = UNSET
    map_sides: Union[Unset, List[MapSidesEnum]] = UNSET
    clinch_series: Union[Unset, bool] = UNSET
    cvars: Union[Unset, "MatchUpdateCvars"] = UNSET
    message_id: Union[Unset, str] = UNSET
    author_id: Union[Unset, str] = UNSET
    server_id: Union[Unset, str] = UNSET
    guild_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        team1_id = self.team1_id

        team2_id = self.team2_id

        map_sides: Union[Unset, List[str]] = UNSET
        if not isinstance(self.map_sides, Unset):
            map_sides = []
            for map_sides_item_data in self.map_sides:
                map_sides_item = map_sides_item_data.value
                map_sides.append(map_sides_item)

        clinch_series = self.clinch_series

        cvars: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cvars, Unset):
            cvars = self.cvars.to_dict()

        message_id = self.message_id

        author_id = self.author_id

        server_id = self.server_id

        guild_id = self.guild_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if team1_id is not UNSET:
            field_dict["team1_id"] = team1_id
        if team2_id is not UNSET:
            field_dict["team2_id"] = team2_id
        if map_sides is not UNSET:
            field_dict["map_sides"] = map_sides
        if clinch_series is not UNSET:
            field_dict["clinch_series"] = clinch_series
        if cvars is not UNSET:
            field_dict["cvars"] = cvars
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if server_id is not UNSET:
            field_dict["server_id"] = server_id
        if guild_id is not UNSET:
            field_dict["guild_id"] = guild_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.match_update_cvars import MatchUpdateCvars

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusEnum(_status)

        _type = d.pop("type", UNSET)
        type: Union[Unset, TypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TypeEnum(_type)

        team1_id = d.pop("team1_id", UNSET)

        team2_id = d.pop("team2_id", UNSET)

        map_sides = []
        _map_sides = d.pop("map_sides", UNSET)
        for map_sides_item_data in _map_sides or []:
            map_sides_item = MapSidesEnum(map_sides_item_data)

            map_sides.append(map_sides_item)

        clinch_series = d.pop("clinch_series", UNSET)

        _cvars = d.pop("cvars", UNSET)
        cvars: Union[Unset, MatchUpdateCvars]
        if isinstance(_cvars, Unset):
            cvars = UNSET
        else:
            cvars = MatchUpdateCvars.from_dict(_cvars)

        message_id = d.pop("message_id", UNSET)

        author_id = d.pop("author_id", UNSET)

        server_id = d.pop("server_id", UNSET)

        guild_id = d.pop("guild_id", UNSET)

        match_update = cls(
            status=status,
            type=type,
            team1_id=team1_id,
            team2_id=team2_id,
            map_sides=map_sides,
            clinch_series=clinch_series,
            cvars=cvars,
            message_id=message_id,
            author_id=author_id,
            server_id=server_id,
            guild_id=guild_id,
        )

        match_update.additional_properties = d
        return match_update

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
