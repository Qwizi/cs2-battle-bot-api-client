import datetime
import json
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import Unset

if TYPE_CHECKING:
    from ..models.nested import Nested


T = TypeVar("T", bound="Player")


@_attrs_define
class Player:
    """
    Attributes:
        id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        discord_user (Nested):
        steam_user (Nested):
    """

    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    discord_user: "Nested"
    steam_user: "Nested"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        discord_user = self.discord_user.to_dict()

        steam_user = self.steam_user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "discord_user": discord_user,
                "steam_user": steam_user,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        discord_user = (None, json.dumps(self.discord_user.to_dict()).encode(), "application/json")

        steam_user = (None, json.dumps(self.steam_user.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "discord_user": discord_user,
                "steam_user": steam_user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nested import Nested

        d = src_dict.copy()
        id = d.pop("id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        discord_user = Nested.from_dict(d.pop("discord_user"))

        steam_user = Nested.from_dict(d.pop("steam_user"))

        player = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            discord_user=discord_user,
            steam_user=steam_user,
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
