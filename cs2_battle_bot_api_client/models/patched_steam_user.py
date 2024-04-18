import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSteamUser")


@_attrs_define
class PatchedSteamUser:
    """
    Attributes:
        id (Union[Unset, str]):
        username (Union[Unset, str]):
        steamid64 (Union[None, Unset, str]):
        steamid32 (Union[None, Unset, str]):
        profile_url (Union[None, Unset, str]):
        avatar (Union[None, Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    steamid64: Union[None, Unset, str] = UNSET
    steamid32: Union[None, Unset, str] = UNSET
    profile_url: Union[None, Unset, str] = UNSET
    avatar: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        username = self.username

        steamid64: Union[None, Unset, str]
        if isinstance(self.steamid64, Unset):
            steamid64 = UNSET
        else:
            steamid64 = self.steamid64

        steamid32: Union[None, Unset, str]
        if isinstance(self.steamid32, Unset):
            steamid32 = UNSET
        else:
            steamid32 = self.steamid32

        profile_url: Union[None, Unset, str]
        if isinstance(self.profile_url, Unset):
            profile_url = UNSET
        else:
            profile_url = self.profile_url

        avatar: Union[None, Unset, str]
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

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
        if username is not UNSET:
            field_dict["username"] = username
        if steamid64 is not UNSET:
            field_dict["steamid64"] = steamid64
        if steamid32 is not UNSET:
            field_dict["steamid32"] = steamid32
        if profile_url is not UNSET:
            field_dict["profile_url"] = profile_url
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        def _parse_steamid64(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        steamid64 = _parse_steamid64(d.pop("steamid64", UNSET))

        def _parse_steamid32(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        steamid32 = _parse_steamid32(d.pop("steamid32", UNSET))

        def _parse_profile_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        profile_url = _parse_profile_url(d.pop("profile_url", UNSET))

        def _parse_avatar(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

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

        patched_steam_user = cls(
            id=id,
            username=username,
            steamid64=steamid64,
            steamid32=steamid32,
            profile_url=profile_url,
            avatar=avatar,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_steam_user.additional_properties = d
        return patched_steam_user

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
