import datetime
import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.status_enum import StatusEnum
from ..models.type_enum import TypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.guild import Guild
    from ..models.map_ import Map
    from ..models.map_ban import MapBan
    from ..models.match_map_selected import MatchMapSelected
    from ..models.server import Server
    from ..models.team import Team


T = TypeVar("T", bound="Match")


@_attrs_define
class Match:
    """
    Attributes:
        id (int):
        team1 (Team):
        team2 (Team):
        winner_team (Team):
        maps (List['Map']):
        map_bans (List['MapBan']):
        map_picks (List['MatchMapSelected']):
        connect_command (str):
        load_match_command (str):
        server (Server):
        guild (Guild):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        status (Union[Unset, StatusEnum]): * `CREATED` - Created
            * `STARTED` - Started
            * `LIVE` - Live
            * `FINISHED` - Finished
        type (Union[Unset, TypeEnum]): * `BO1` - Bo1
            * `BO3` - Bo3
            * `BO5` - Bo5
        num_maps (Union[Unset, int]):
        maplist (Union[Unset, Any]):
        map_sides (Union[Unset, Any]):
        clinch_series (Union[Unset, bool]):
        cvars (Union[Unset, Any]):
        players_per_team (Union[Unset, int]):
        message_id (Union[None, Unset, str]):
        author (Union[None, Unset, str]):
    """

    id: int
    team1: "Team"
    team2: "Team"
    winner_team: "Team"
    maps: List["Map"]
    map_bans: List["MapBan"]
    map_picks: List["MatchMapSelected"]
    connect_command: str
    load_match_command: str
    server: "Server"
    guild: "Guild"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    status: Union[Unset, StatusEnum] = UNSET
    type: Union[Unset, TypeEnum] = UNSET
    num_maps: Union[Unset, int] = UNSET
    maplist: Union[Unset, Any] = UNSET
    map_sides: Union[Unset, Any] = UNSET
    clinch_series: Union[Unset, bool] = UNSET
    cvars: Union[Unset, Any] = UNSET
    players_per_team: Union[Unset, int] = UNSET
    message_id: Union[None, Unset, str] = UNSET
    author: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        team1 = self.team1.to_dict()

        team2 = self.team2.to_dict()

        winner_team = self.winner_team.to_dict()

        maps = []
        for maps_item_data in self.maps:
            maps_item = maps_item_data.to_dict()
            maps.append(maps_item)

        map_bans = []
        for map_bans_item_data in self.map_bans:
            map_bans_item = map_bans_item_data.to_dict()
            map_bans.append(map_bans_item)

        map_picks = []
        for map_picks_item_data in self.map_picks:
            map_picks_item = map_picks_item_data.to_dict()
            map_picks.append(map_picks_item)

        connect_command = self.connect_command

        load_match_command = self.load_match_command

        server = self.server.to_dict()

        guild = self.guild.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        num_maps = self.num_maps

        maplist = self.maplist

        map_sides = self.map_sides

        clinch_series = self.clinch_series

        cvars = self.cvars

        players_per_team = self.players_per_team

        message_id: Union[None, Unset, str]
        if isinstance(self.message_id, Unset):
            message_id = UNSET
        else:
            message_id = self.message_id

        author: Union[None, Unset, str]
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "team1": team1,
                "team2": team2,
                "winner_team": winner_team,
                "maps": maps,
                "map_bans": map_bans,
                "map_picks": map_picks,
                "connect_command": connect_command,
                "load_match_command": load_match_command,
                "server": server,
                "guild": guild,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if num_maps is not UNSET:
            field_dict["num_maps"] = num_maps
        if maplist is not UNSET:
            field_dict["maplist"] = maplist
        if map_sides is not UNSET:
            field_dict["map_sides"] = map_sides
        if clinch_series is not UNSET:
            field_dict["clinch_series"] = clinch_series
        if cvars is not UNSET:
            field_dict["cvars"] = cvars
        if players_per_team is not UNSET:
            field_dict["players_per_team"] = players_per_team
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        team1 = (None, json.dumps(self.team1.to_dict()).encode(), "application/json")

        team2 = (None, json.dumps(self.team2.to_dict()).encode(), "application/json")

        winner_team = (None, json.dumps(self.winner_team.to_dict()).encode(), "application/json")

        _temp_maps = []
        for maps_item_data in self.maps:
            maps_item = maps_item_data.to_dict()
            _temp_maps.append(maps_item)
        maps = (None, json.dumps(_temp_maps).encode(), "application/json")

        _temp_map_bans = []
        for map_bans_item_data in self.map_bans:
            map_bans_item = map_bans_item_data.to_dict()
            _temp_map_bans.append(map_bans_item)
        map_bans = (None, json.dumps(_temp_map_bans).encode(), "application/json")

        _temp_map_picks = []
        for map_picks_item_data in self.map_picks:
            map_picks_item = map_picks_item_data.to_dict()
            _temp_map_picks.append(map_picks_item)
        map_picks = (None, json.dumps(_temp_map_picks).encode(), "application/json")

        connect_command = (
            self.connect_command
            if isinstance(self.connect_command, Unset)
            else (None, str(self.connect_command).encode(), "text/plain")
        )

        load_match_command = (
            self.load_match_command
            if isinstance(self.load_match_command, Unset)
            else (None, str(self.load_match_command).encode(), "text/plain")
        )

        server = (None, json.dumps(self.server.to_dict()).encode(), "application/json")

        guild = (None, json.dumps(self.guild.to_dict()).encode(), "application/json")

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        status: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        type: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.type, Unset):
            type = (None, str(self.type.value).encode(), "text/plain")

        num_maps = (
            self.num_maps if isinstance(self.num_maps, Unset) else (None, str(self.num_maps).encode(), "text/plain")
        )

        maplist = self.maplist if isinstance(self.maplist, Unset) else (None, str(self.maplist).encode(), "text/plain")

        map_sides = (
            self.map_sides if isinstance(self.map_sides, Unset) else (None, str(self.map_sides).encode(), "text/plain")
        )

        clinch_series = (
            self.clinch_series
            if isinstance(self.clinch_series, Unset)
            else (None, str(self.clinch_series).encode(), "text/plain")
        )

        cvars = self.cvars if isinstance(self.cvars, Unset) else (None, str(self.cvars).encode(), "text/plain")

        players_per_team = (
            self.players_per_team
            if isinstance(self.players_per_team, Unset)
            else (None, str(self.players_per_team).encode(), "text/plain")
        )

        message_id: Union[None, Unset, str]
        if isinstance(self.message_id, Unset):
            message_id = UNSET
        else:
            message_id = self.message_id

        author: Union[None, Unset, str]
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "team1": team1,
                "team2": team2,
                "winner_team": winner_team,
                "maps": maps,
                "map_bans": map_bans,
                "map_picks": map_picks,
                "connect_command": connect_command,
                "load_match_command": load_match_command,
                "server": server,
                "guild": guild,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if num_maps is not UNSET:
            field_dict["num_maps"] = num_maps
        if maplist is not UNSET:
            field_dict["maplist"] = maplist
        if map_sides is not UNSET:
            field_dict["map_sides"] = map_sides
        if clinch_series is not UNSET:
            field_dict["clinch_series"] = clinch_series
        if cvars is not UNSET:
            field_dict["cvars"] = cvars
        if players_per_team is not UNSET:
            field_dict["players_per_team"] = players_per_team
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.guild import Guild
        from ..models.map_ import Map
        from ..models.map_ban import MapBan
        from ..models.match_map_selected import MatchMapSelected
        from ..models.server import Server
        from ..models.team import Team

        d = src_dict.copy()
        id = d.pop("id")

        team1 = Team.from_dict(d.pop("team1"))

        team2 = Team.from_dict(d.pop("team2"))

        winner_team = Team.from_dict(d.pop("winner_team"))

        maps = []
        _maps = d.pop("maps")
        for maps_item_data in _maps:
            maps_item = Map.from_dict(maps_item_data)

            maps.append(maps_item)

        map_bans = []
        _map_bans = d.pop("map_bans")
        for map_bans_item_data in _map_bans:
            map_bans_item = MapBan.from_dict(map_bans_item_data)

            map_bans.append(map_bans_item)

        map_picks = []
        _map_picks = d.pop("map_picks")
        for map_picks_item_data in _map_picks:
            map_picks_item = MatchMapSelected.from_dict(map_picks_item_data)

            map_picks.append(map_picks_item)

        connect_command = d.pop("connect_command")

        load_match_command = d.pop("load_match_command")

        server = Server.from_dict(d.pop("server"))

        guild = Guild.from_dict(d.pop("guild"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusEnum(_status)

        _type = d.pop("type", UNSET)
        type: Union[Unset, TypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TypeEnum(_type)

        num_maps = d.pop("num_maps", UNSET)

        maplist = d.pop("maplist", UNSET)

        map_sides = d.pop("map_sides", UNSET)

        clinch_series = d.pop("clinch_series", UNSET)

        cvars = d.pop("cvars", UNSET)

        players_per_team = d.pop("players_per_team", UNSET)

        def _parse_message_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message_id = _parse_message_id(d.pop("message_id", UNSET))

        def _parse_author(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        author = _parse_author(d.pop("author", UNSET))

        match = cls(
            id=id,
            team1=team1,
            team2=team2,
            winner_team=winner_team,
            maps=maps,
            map_bans=map_bans,
            map_picks=map_picks,
            connect_command=connect_command,
            load_match_command=load_match_command,
            server=server,
            guild=guild,
            created_at=created_at,
            updated_at=updated_at,
            status=status,
            type=type,
            num_maps=num_maps,
            maplist=maplist,
            map_sides=map_sides,
            clinch_series=clinch_series,
            cvars=cvars,
            players_per_team=players_per_team,
            message_id=message_id,
            author=author,
        )

        match.additional_properties = d
        return match

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
