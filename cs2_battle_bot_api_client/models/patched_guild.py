import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedGuild")


@_attrs_define
class PatchedGuild:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        guild_id (Union[Unset, str]):
        lobby_channel (Union[None, Unset, str]):
        team1_channel (Union[None, Unset, str]):
        team2_channel (Union[None, Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        owner (Union[Unset, str]):
        members (Union[Unset, List[str]]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    guild_id: Union[Unset, str] = UNSET
    lobby_channel: Union[None, Unset, str] = UNSET
    team1_channel: Union[None, Unset, str] = UNSET
    team2_channel: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    owner: Union[Unset, str] = UNSET
    members: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        guild_id = self.guild_id

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

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        owner = self.owner

        members: Union[Unset, List[str]] = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if guild_id is not UNSET:
            field_dict["guild_id"] = guild_id
        if lobby_channel is not UNSET:
            field_dict["lobby_channel"] = lobby_channel
        if team1_channel is not UNSET:
            field_dict["team1_channel"] = team1_channel
        if team2_channel is not UNSET:
            field_dict["team2_channel"] = team2_channel
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if owner is not UNSET:
            field_dict["owner"] = owner
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        guild_id = d.pop("guild_id", UNSET)

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

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        owner = d.pop("owner", UNSET)

        members = cast(List[str], d.pop("members", UNSET))

        patched_guild = cls(
            id=id,
            name=name,
            guild_id=guild_id,
            lobby_channel=lobby_channel,
            team1_channel=team1_channel,
            team2_channel=team2_channel,
            created_at=created_at,
            updated_at=updated_at,
            owner=owner,
            members=members,
        )

        patched_guild.additional_properties = d
        return patched_guild

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
