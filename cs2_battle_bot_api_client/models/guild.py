import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="Guild")


@_attrs_define
class Guild:
    """
    Attributes:
        id (str):
        owner (User):
        name (str):
        guild_id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        lobby_channel (Union[None, Unset, str]):
        team1_channel (Union[None, Unset, str]):
        team2_channel (Union[None, Unset, str]):
    """

    id: str
    owner: "User"
    name: str
    guild_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    lobby_channel: Union[None, Unset, str] = UNSET
    team1_channel: Union[None, Unset, str] = UNSET
    team2_channel: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        owner = self.owner.to_dict()

        name = self.name

        guild_id = self.guild_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        lobby_channel: Union[None, Unset, str]
        if isinstance(self.lobby_channel, Unset):
            lobby_channel = UNSET
        else:
            lobby_channel = self.lobby_channel

        team1_channel: Union[None, Unset, str]
        if isinstance(self.team1_channel, Unset):
            team1_channel = UNSET
        else:
            team1_channel = self.team1_channel

        team2_channel: Union[None, Unset, str]
        if isinstance(self.team2_channel, Unset):
            team2_channel = UNSET
        else:
            team2_channel = self.team2_channel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "owner": owner,
                "name": name,
                "guild_id": guild_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if lobby_channel is not UNSET:
            field_dict["lobby_channel"] = lobby_channel
        if team1_channel is not UNSET:
            field_dict["team1_channel"] = team1_channel
        if team2_channel is not UNSET:
            field_dict["team2_channel"] = team2_channel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user import User

        d = src_dict.copy()
        id = d.pop("id")

        owner = User.from_dict(d.pop("owner"))

        name = d.pop("name")

        guild_id = d.pop("guild_id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_lobby_channel(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        lobby_channel = _parse_lobby_channel(d.pop("lobby_channel", UNSET))

        def _parse_team1_channel(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        team1_channel = _parse_team1_channel(d.pop("team1_channel", UNSET))

        def _parse_team2_channel(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        team2_channel = _parse_team2_channel(d.pop("team2_channel", UNSET))

        guild = cls(
            id=id,
            owner=owner,
            name=name,
            guild_id=guild_id,
            created_at=created_at,
            updated_at=updated_at,
            lobby_channel=lobby_channel,
            team1_channel=team1_channel,
            team2_channel=team2_channel,
        )

        guild.additional_properties = d
        return guild

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
