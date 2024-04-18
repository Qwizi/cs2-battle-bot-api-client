import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player import Player


T = TypeVar("T", bound="PatchedTeam")


@_attrs_define
class PatchedTeam:
    """
    Attributes:
        id (Union[Unset, str]):
        players (Union[Unset, List['Player']]):
        leader (Union[Unset, Player]):
        name (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    players: Union[Unset, List["Player"]] = UNSET
    leader: Union[Unset, "Player"] = UNSET
    name: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        players: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.players, Unset):
            players = []
            for players_item_data in self.players:
                players_item = players_item_data.to_dict()
                players.append(players_item)

        leader: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leader, Unset):
            leader = self.leader.to_dict()

        name = self.name

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if players is not UNSET:
            field_dict["players"] = players
        if leader is not UNSET:
            field_dict["leader"] = leader
        if name is not UNSET:
            field_dict["name"] = name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player import Player

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        players = []
        _players = d.pop("players", UNSET)
        for players_item_data in _players or []:
            players_item = Player.from_dict(players_item_data)

            players.append(players_item)

        _leader = d.pop("leader", UNSET)
        leader: Union[Unset, Player]
        if isinstance(_leader, Unset):
            leader = UNSET
        else:
            leader = Player.from_dict(_leader)

        name = d.pop("name", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        patched_team = cls(
            id=id,
            players=players,
            leader=leader,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_team.additional_properties = d
        return patched_team

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
