from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Server")


@_attrs_define
class Server:
    """
    Attributes:
        id (str):
        name (str):
        ip (str):
        port (int):
        join_url (str):
        password (Union[None, Unset, str]):
        is_public (Union[Unset, bool]):
        rcon_password (Union[Unset, str]):
        guild (Union[None, Unset, str]):
    """

    id: str
    name: str
    ip: str
    port: int
    join_url: str
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

        join_url = self.join_url

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
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ip": ip,
                "port": port,
                "join_url": join_url,
            }
        )
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
        id = d.pop("id")

        name = d.pop("name")

        ip = d.pop("ip")

        port = d.pop("port")

        join_url = d.pop("join_url")

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

        server = cls(
            id=id,
            name=name,
            ip=ip,
            port=port,
            join_url=join_url,
            password=password,
            is_public=is_public,
            rcon_password=rcon_password,
            guild=guild,
        )

        server.additional_properties = d
        return server

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
