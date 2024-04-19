from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import Union
from typing import cast
from typing import cast, List
from typing import cast, Union
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.player import Player





T = TypeVar("T", bound="PaginatedPlayerList")


@_attrs_define
class PaginatedPlayerList:
    """ 
        Attributes:
            count (int):  Example: 123.
            results (List['Player']):
            next_ (Union[None, Unset, str]):  Example: http://api.example.org/accounts/?page=4.
            previous (Union[None, Unset, str]):  Example: http://api.example.org/accounts/?page=2.
     """

    count: int
    results: List['Player']
    next_: Union[None, Unset, str] = UNSET
    previous: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.player import Player
        count = self.count

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)





        next_: Union[None, Unset, str]
        if isinstance(self.next_, Unset):
            next_ = UNSET
        else:
            next_ = self.next_

        previous: Union[None, Unset, str]
        if isinstance(self.previous, Unset):
            previous = UNSET
        else:
            previous = self.previous


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "count": count,
            "results": results,
        })
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player import Player
        d = src_dict.copy()
        count = d.pop("count")

        results = []
        _results = d.pop("results")
        for results_item_data in (_results):
            results_item = Player.from_dict(results_item_data)



            results.append(results_item)


        def _parse_next_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_ = _parse_next_(d.pop("next", UNSET))


        def _parse_previous(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        previous = _parse_previous(d.pop("previous", UNSET))


        paginated_player_list = cls(
            count=count,
            results=results,
            next_=next_,
            previous=previous,
        )

        paginated_player_list.additional_properties = d
        return paginated_player_list

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
