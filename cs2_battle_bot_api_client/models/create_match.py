from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.map_sides_enum import MapSidesEnum
from ..models.match_type_enum import MatchTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_match_cvars import CreateMatchCvars


T = TypeVar("T", bound="CreateMatch")


@_attrs_define
class CreateMatch:
    """
    Attributes:
        discord_users_ids (List[str]):
        author_id (str):
        guild_id (str):
        server_id (Union[Unset, str]):
        match_type (Union[Unset, MatchTypeEnum]): * `BO1` - Bo1
            * `BO3` - Bo3
            * `BO5` - Bo5 Default: MatchTypeEnum.BO1.
        clinch_series (Union[Unset, bool]):  Default: False.
        map_sides (Union[Unset, List[MapSidesEnum]]):
        cvars (Union[Unset, CreateMatchCvars]):
    """

    discord_users_ids: List[str]
    author_id: str
    guild_id: str
    server_id: Union[Unset, str] = UNSET
    match_type: Union[Unset, MatchTypeEnum] = MatchTypeEnum.BO1
    clinch_series: Union[Unset, bool] = False
    map_sides: Union[Unset, List[MapSidesEnum]] = UNSET
    cvars: Union[Unset, "CreateMatchCvars"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        discord_users_ids = self.discord_users_ids

        author_id = self.author_id

        guild_id = self.guild_id

        server_id = self.server_id

        match_type: Union[Unset, str] = UNSET
        if not isinstance(self.match_type, Unset):
            match_type = self.match_type.value

        clinch_series = self.clinch_series

        map_sides: Union[Unset, List[str]] = UNSET
        if not isinstance(self.map_sides, Unset):
            map_sides = []
            for map_sides_item_data in self.map_sides:
                map_sides_item = map_sides_item_data.value
                map_sides.append(map_sides_item)

        cvars: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cvars, Unset):
            cvars = self.cvars.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "discord_users_ids": discord_users_ids,
                "author_id": author_id,
                "guild_id": guild_id,
            }
        )
        if server_id is not UNSET:
            field_dict["server_id"] = server_id
        if match_type is not UNSET:
            field_dict["match_type"] = match_type
        if clinch_series is not UNSET:
            field_dict["clinch_series"] = clinch_series
        if map_sides is not UNSET:
            field_dict["map_sides"] = map_sides
        if cvars is not UNSET:
            field_dict["cvars"] = cvars

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_match_cvars import CreateMatchCvars

        d = src_dict.copy()
        discord_users_ids = cast(List[str], d.pop("discord_users_ids"))

        author_id = d.pop("author_id")

        guild_id = d.pop("guild_id")

        server_id = d.pop("server_id", UNSET)

        _match_type = d.pop("match_type", UNSET)
        match_type: Union[Unset, MatchTypeEnum]
        if isinstance(_match_type, Unset):
            match_type = UNSET
        else:
            match_type = MatchTypeEnum(_match_type)

        clinch_series = d.pop("clinch_series", UNSET)

        map_sides = []
        _map_sides = d.pop("map_sides", UNSET)
        for map_sides_item_data in _map_sides or []:
            map_sides_item = MapSidesEnum(map_sides_item_data)

            map_sides.append(map_sides_item)

        _cvars = d.pop("cvars", UNSET)
        cvars: Union[Unset, CreateMatchCvars]
        if isinstance(_cvars, Unset):
            cvars = UNSET
        else:
            cvars = CreateMatchCvars.from_dict(_cvars)

        create_match = cls(
            discord_users_ids=discord_users_ids,
            author_id=author_id,
            guild_id=guild_id,
            server_id=server_id,
            match_type=match_type,
            clinch_series=clinch_series,
            map_sides=map_sides,
            cvars=cvars,
        )

        create_match.additional_properties = d
        return create_match

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
