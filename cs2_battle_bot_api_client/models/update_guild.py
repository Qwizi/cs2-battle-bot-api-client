from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateGuild")


@_attrs_define
class UpdateGuild:
    """
    Attributes:
        name (Union[Unset, str]):
        lobby_channel (Union[Unset, str]):
        team1_channel (Union[Unset, str]):
        team2_channel (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    lobby_channel: Union[Unset, str] = UNSET
    team1_channel: Union[Unset, str] = UNSET
    team2_channel: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        lobby_channel = self.lobby_channel

        team1_channel = self.team1_channel

        team2_channel = self.team2_channel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if lobby_channel is not UNSET:
            field_dict["lobby_channel"] = lobby_channel
        if team1_channel is not UNSET:
            field_dict["team1_channel"] = team1_channel
        if team2_channel is not UNSET:
            field_dict["team2_channel"] = team2_channel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        lobby_channel = d.pop("lobby_channel", UNSET)

        team1_channel = d.pop("team1_channel", UNSET)

        team2_channel = d.pop("team2_channel", UNSET)

        update_guild = cls(
            name=name,
            lobby_channel=lobby_channel,
            team1_channel=team1_channel,
            team2_channel=team2_channel,
        )

        update_guild.additional_properties = d
        return update_guild

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
