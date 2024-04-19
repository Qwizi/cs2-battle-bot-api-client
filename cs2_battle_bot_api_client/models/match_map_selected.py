from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from typing import cast
from dateutil.parser import isoparse
from typing import Dict

if TYPE_CHECKING:
  from ..models.team import Team
  from ..models.map_ import Map





T = TypeVar("T", bound="MatchMapSelected")


@_attrs_define
class MatchMapSelected:
    """ 
        Attributes:
            id (int):
            team (Team):
            map_ (Map):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
     """

    id: int
    team: 'Team'
    map_: 'Map'
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.team import Team
        from ..models.map_ import Map
        id = self.id

        team = self.team.to_dict()

        map_ = self.map_.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "team": team,
            "map": map_,
            "created_at": created_at,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team import Team
        from ..models.map_ import Map
        d = src_dict.copy()
        id = d.pop("id")

        team = Team.from_dict(d.pop("team"))




        map_ = Map.from_dict(d.pop("map"))




        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        match_map_selected = cls(
            id=id,
            team=team,
            map_=map_,
            created_at=created_at,
            updated_at=updated_at,
        )

        match_map_selected.additional_properties = d
        return match_map_selected

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
