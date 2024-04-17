import datetime
import json
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player import Player


T = TypeVar("T", bound="Team")


@_attrs_define
class Team:
    """
    Attributes:
        id (str):
        players (List['Player']):
        name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        leader (Union[None, Unset, str]):
    """

    id: str
    players: List["Player"]
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    leader: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)

        name = self.name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        leader: Union[None, Unset, str]
        if isinstance(self.leader, Unset):
            leader = UNSET
        else:
            leader = self.leader

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "players": players,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if leader is not UNSET:
            field_dict["leader"] = leader

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        _temp_players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            _temp_players.append(players_item)
        players = (None, json.dumps(_temp_players).encode(), "application/json")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        leader: Union[None, Unset, str]
        if isinstance(self.leader, Unset):
            leader = UNSET
        else:
            leader = self.leader

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "players": players,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if leader is not UNSET:
            field_dict["leader"] = leader

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player import Player

        d = src_dict.copy()
        id = d.pop("id")

        players = []
        _players = d.pop("players")
        for players_item_data in _players:
            players_item = Player.from_dict(players_item_data)

            players.append(players_item)

        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_leader(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        leader = _parse_leader(d.pop("leader", UNSET))

        team = cls(
            id=id,
            players=players,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            leader=leader,
        )

        team.additional_properties = d
        return team

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
