from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast
import datetime
from dateutil.parser import isoparse
from typing import cast, Union
from ..types import UNSET, Unset






T = TypeVar("T", bound="SteamUser")


@_attrs_define
class SteamUser:
    """ 
        Attributes:
            id (str):
            username (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            steamid64 (Union[None, Unset, str]):
            steamid32 (Union[None, Unset, str]):
            profile_url (Union[None, Unset, str]):
            avatar (Union[None, Unset, str]):
     """

    id: str
    username: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    steamid64: Union[None, Unset, str] = UNSET
    steamid32: Union[None, Unset, str] = UNSET
    profile_url: Union[None, Unset, str] = UNSET
    avatar: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        username = self.username

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "username": username,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if steamid64 is not UNSET:
            field_dict["steamid64"] = steamid64
        if steamid32 is not UNSET:
            field_dict["steamid32"] = steamid32
        if profile_url is not UNSET:
            field_dict["profile_url"] = profile_url
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        username = d.pop("username")

        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




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


        steam_user = cls(
            id=id,
            username=username,
            created_at=created_at,
            updated_at=updated_at,
            steamid64=steamid64,
            steamid32=steamid32,
            profile_url=profile_url,
            avatar=avatar,
        )

        steam_user.additional_properties = d
        return steam_user

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
