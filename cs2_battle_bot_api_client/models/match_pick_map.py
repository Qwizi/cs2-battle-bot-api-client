from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import Unset

T = TypeVar("T", bound="MatchPickMap")


@_attrs_define
class MatchPickMap:
    """
    Attributes:
        interaction_user_id (str):
        map_tag (str):
    """

    interaction_user_id: str
    map_tag: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interaction_user_id = self.interaction_user_id

        map_tag = self.map_tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interaction_user_id": interaction_user_id,
                "map_tag": map_tag,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        interaction_user_id = (
            self.interaction_user_id
            if isinstance(self.interaction_user_id, Unset)
            else (None, str(self.interaction_user_id).encode(), "text/plain")
        )

        map_tag = self.map_tag if isinstance(self.map_tag, Unset) else (None, str(self.map_tag).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "interaction_user_id": interaction_user_id,
                "map_tag": map_tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interaction_user_id = d.pop("interaction_user_id")

        map_tag = d.pop("map_tag")

        match_pick_map = cls(
            interaction_user_id=interaction_user_id,
            map_tag=map_tag,
        )

        match_pick_map.additional_properties = d
        return match_pick_map

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
