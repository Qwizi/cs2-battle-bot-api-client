import datetime
import json
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Guild")


@_attrs_define
class Guild:
    """
    Attributes:
        id (str):
        name (str):
        guild_id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        owner (str):
        members (List[str]):
        lobby_channel (Union[None, Unset, str]):
        team1_channel (Union[None, Unset, str]):
        team2_channel (Union[None, Unset, str]):
    """

    id: str
    name: str
    guild_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    owner: str
    members: List[str]
    lobby_channel: Union[None, Unset, str] = UNSET
    team1_channel: Union[None, Unset, str] = UNSET
    team2_channel: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        guild_id = self.guild_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        owner = self.owner

        members = self.members

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
                "name": name,
                "guild_id": guild_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "owner": owner,
                "members": members,
            }
        )
        if lobby_channel is not UNSET:
            field_dict["lobby_channel"] = lobby_channel
        if team1_channel is not UNSET:
            field_dict["team1_channel"] = team1_channel
        if team2_channel is not UNSET:
            field_dict["team2_channel"] = team2_channel

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        guild_id = (
            self.guild_id if isinstance(self.guild_id, Unset) else (None, str(self.guild_id).encode(), "text/plain")
        )

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        owner = self.owner if isinstance(self.owner, Unset) else (None, str(self.owner).encode(), "text/plain")

        _temp_members = self.members
        members = (None, json.dumps(_temp_members).encode(), "application/json")

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
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "name": name,
                "guild_id": guild_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "owner": owner,
                "members": members,
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
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        guild_id = d.pop("guild_id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        owner = d.pop("owner")

        members = cast(List[str], d.pop("members"))

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
            name=name,
            guild_id=guild_id,
            created_at=created_at,
            updated_at=updated_at,
            owner=owner,
            members=members,
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
