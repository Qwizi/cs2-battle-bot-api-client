from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, List
from typing import Dict

if TYPE_CHECKING:
  from ..models.create_guild_member import CreateGuildMember





T = TypeVar("T", bound="CreateGuild")


@_attrs_define
class CreateGuild:
    """ 
        Attributes:
            name (str):
            guild_id (str):
            owner_id (str):
            owner_username (str):
            members (List['CreateGuildMember']):
     """

    name: str
    guild_id: str
    owner_id: str
    owner_username: str
    members: List['CreateGuildMember']
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.create_guild_member import CreateGuildMember
        name = self.name

        guild_id = self.guild_id

        owner_id = self.owner_id

        owner_username = self.owner_username

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)






        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "guild_id": guild_id,
            "owner_id": owner_id,
            "owner_username": owner_username,
            "members": members,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_guild_member import CreateGuildMember
        d = src_dict.copy()
        name = d.pop("name")

        guild_id = d.pop("guild_id")

        owner_id = d.pop("owner_id")

        owner_username = d.pop("owner_username")

        members = []
        _members = d.pop("members")
        for members_item_data in (_members):
            members_item = CreateGuildMember.from_dict(members_item_data)



            members.append(members_item)


        create_guild = cls(
            name=name,
            guild_id=guild_id,
            owner_id=owner_id,
            owner_username=owner_username,
            members=members,
        )

        create_guild.additional_properties = d
        return create_guild

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
