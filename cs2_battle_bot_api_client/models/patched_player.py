import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        steam_user (Union['SteamUser', None, Unset]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    discord_user: Union[Unset, "DiscordUser"] = UNSET
    steam_user: Union["SteamUser", None, Unset] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.steam_user import SteamUser

        id = self.id

        discord_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discord_user, Unset):
            discord_user = self.discord_user.to_dict()

        steam_user: Union[Dict[str, Any], None, Unset]
        if isinstance(self.steam_user, Unset):
            steam_user = UNSET
        elif isinstance(self.steam_user, SteamUser):
            steam_user = self.steam_user.to_dict()
        else:
            steam_user = self.steam_user

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

        def _parse_steam_user(data: object) -> Union["SteamUser", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                steam_user_type_1 = SteamUser.from_dict(data)

                return steam_user_type_1
            except:  # noqa: E722
                pass
            return cast(Union["SteamUser", None, Unset], data)

        steam_user = _parse_steam_user(d.pop("steam_user", UNSET))

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
