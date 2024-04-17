from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedServer")


@_attrs_define
class PatchedServer:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        ip (Union[Unset, str]):
        port (Union[Unset, int]):
        password (Union[None, Unset, str]):
        is_public (Union[Unset, bool]):
        rcon_password (Union[Unset, str]):
        guild (Union[None, Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    password: Union[None, Unset, str] = UNSET
    is_public: Union[Unset, bool] = UNSET
    rcon_password: Union[Unset, str] = UNSET
    guild: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        ip = self.ip

        port = self.port

        password: Union[None, Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        is_public = self.is_public

        rcon_password = self.rcon_password

        guild: Union[None, Unset, str]
        if isinstance(self.guild, Unset):
            guild = UNSET
        else:
            guild = self.guild

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if port is not UNSET:
            field_dict["port"] = port
        if password is not UNSET:
            field_dict["password"] = password
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if rcon_password is not UNSET:
            field_dict["rcon_password"] = rcon_password
        if guild is not UNSET:
            field_dict["guild"] = guild

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        ip = self.ip if isinstance(self.ip, Unset) else (None, str(self.ip).encode(), "text/plain")

        port = self.port if isinstance(self.port, Unset) else (None, str(self.port).encode(), "text/plain")

        password: Union[None, Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        is_public = (
            self.is_public if isinstance(self.is_public, Unset) else (None, str(self.is_public).encode(), "text/plain")
        )

        rcon_password = (
            self.rcon_password
            if isinstance(self.rcon_password, Unset)
            else (None, str(self.rcon_password).encode(), "text/plain")
        )

        guild: Union[None, Unset, str]
        if isinstance(self.guild, Unset):
            guild = UNSET
        else:
            guild = self.guild

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if port is not UNSET:
            field_dict["port"] = port
        if password is not UNSET:
            field_dict["password"] = password
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if rcon_password is not UNSET:
            field_dict["rcon_password"] = rcon_password
        if guild is not UNSET:
            field_dict["guild"] = guild

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        port = d.pop("port", UNSET)

        def _parse_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password = _parse_password(d.pop("password", UNSET))

        is_public = d.pop("is_public", UNSET)

        rcon_password = d.pop("rcon_password", UNSET)

        def _parse_guild(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        guild = _parse_guild(d.pop("guild", UNSET))

        patched_server = cls(
            id=id,
            name=name,
            ip=ip,
            port=port,
            password=password,
            is_public=is_public,
            rcon_password=rcon_password,
            guild=guild,
        )

        patched_server.additional_properties = d
        return patched_server

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
