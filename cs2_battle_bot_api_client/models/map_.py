from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from typing import cast
from dateutil.parser import isoparse






T = TypeVar("T", bound="Map")


@_attrs_define
class Map:
    """ 
        Attributes:
            id (str):
            name (str):
            tag (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
     """

    id: str
    name: str
    tag: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        tag = self.tag

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "tag": tag,
            "created_at": created_at,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        tag = d.pop("tag")

        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        map_ = cls(
            id=id,
            name=name,
            tag=tag,
            created_at=created_at,
            updated_at=updated_at,
        )

        map_.additional_properties = d
        return map_

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
