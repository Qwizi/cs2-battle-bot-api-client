import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.player import Player


T = TypeVar("T", bound="Team")


@_attrs_define
class Team:
    """
    Attributes:
        id (str):
        players (List['Player']):
        leader (Player):
        name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: str
    players: List["Player"]
    leader: "Player"
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)

        leader = self.leader.to_dict()

        name = self.name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "players": players,
                "leader": leader,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

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

        leader = Player.from_dict(d.pop("leader"))

        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        team = cls(
            id=id,
            players=players,
            leader=leader,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
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
