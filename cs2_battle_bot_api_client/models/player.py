import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.discord_user import DiscordUser
    from ..models.steam_user import SteamUser


T = TypeVar("T", bound="Player")


@_attrs_define
class Player:
    """
    Attributes:
        id (str):
        discord_user (DiscordUser):
        steam_user (Union['SteamUser', None]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: str
    discord_user: "DiscordUser"
    steam_user: Union["SteamUser", None]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.steam_user import SteamUser

        id = self.id

        discord_user = self.discord_user.to_dict()

        steam_user: Union[Dict[str, Any], None]
        if isinstance(self.steam_user, SteamUser):
            steam_user = self.steam_user.to_dict()
        else:
            steam_user = self.steam_user

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "discord_user": discord_user,
                "steam_user": steam_user,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.discord_user import DiscordUser
        from ..models.steam_user import SteamUser

        d = src_dict.copy()
        id = d.pop("id")

        discord_user = DiscordUser.from_dict(d.pop("discord_user"))

        def _parse_steam_user(data: object) -> Union["SteamUser", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                steam_user_type_1 = SteamUser.from_dict(data)

                return steam_user_type_1
            except:  # noqa: E722
                pass
            return cast(Union["SteamUser", None], data)

        steam_user = _parse_steam_user(d.pop("steam_user"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        player = cls(
            id=id,
            discord_user=discord_user,
            steam_user=steam_user,
            created_at=created_at,
            updated_at=updated_at,
        )

        player.additional_properties = d
        return player

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
