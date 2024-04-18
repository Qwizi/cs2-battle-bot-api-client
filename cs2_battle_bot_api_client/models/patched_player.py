import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discord_user import DiscordUser
    from ..models.steam_user import SteamUser


T = TypeVar("T", bound="PatchedPlayer")


@_attrs_define
class PatchedPlayer:
    """
    Attributes:
        id (Union[Unset, str]):
        discord_user (Union[Unset, DiscordUser]):
        steam_user (Union[Unset, SteamUser]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    discord_user: Union[Unset, "DiscordUser"] = UNSET
    steam_user: Union[Unset, "SteamUser"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        discord_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discord_user, Unset):
            discord_user = self.discord_user.to_dict()

        steam_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.steam_user, Unset):
            steam_user = self.steam_user.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if discord_user is not UNSET:
            field_dict["discord_user"] = discord_user
        if steam_user is not UNSET:
            field_dict["steam_user"] = steam_user
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.discord_user import DiscordUser
        from ..models.steam_user import SteamUser

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _discord_user = d.pop("discord_user", UNSET)
        discord_user: Union[Unset, DiscordUser]
        if isinstance(_discord_user, Unset):
            discord_user = UNSET
        else:
            discord_user = DiscordUser.from_dict(_discord_user)

        _steam_user = d.pop("steam_user", UNSET)
        steam_user: Union[Unset, SteamUser]
        if isinstance(_steam_user, Unset):
            steam_user = UNSET
        else:
            steam_user = SteamUser.from_dict(_steam_user)

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

        patched_player = cls(
            id=id,
            discord_user=discord_user,
            steam_user=steam_user,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_player.additional_properties = d
        return patched_player

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
