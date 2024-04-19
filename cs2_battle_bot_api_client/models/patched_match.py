from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import Union
from typing import cast
import datetime
from dateutil.parser import isoparse
from ..models.status_enum import StatusEnum
from typing import cast, List
from typing import cast, Union
from ..models.type_enum import TypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.team import Team
  from ..models.guild import Guild
  from ..models.map_ban import MapBan
  from ..models.server import Server
  from ..models.match_map_selected import MatchMapSelected
  from ..models.map_ import Map





T = TypeVar("T", bound="PatchedMatch")


@_attrs_define
class PatchedMatch:
    """ 
        Attributes:
            id (Union[Unset, int]):
            team1 (Union[Unset, Team]):
            team2 (Union[Unset, Team]):
            maps (Union[Unset, List['Map']]):
            map_bans (Union[Unset, List['MapBan']]):
            map_picks (Union[Unset, List['MatchMapSelected']]):
            connect_command (Union[Unset, str]):
            load_match_command (Union[Unset, str]):
            server (Union[Unset, Server]):
            guild (Union[Unset, Guild]):
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
            created_at (Union[Unset, datetime.datetime]):
            updated_at (Union[Unset, datetime.datetime]):
            winner_team (Union[None, Unset, str]):
            author (Union[None, Unset, str]):
     """

    id: Union[Unset, int] = UNSET
    team1: Union[Unset, 'Team'] = UNSET
    team2: Union[Unset, 'Team'] = UNSET
    maps: Union[Unset, List['Map']] = UNSET
    map_bans: Union[Unset, List['MapBan']] = UNSET
    map_picks: Union[Unset, List['MatchMapSelected']] = UNSET
    connect_command: Union[Unset, str] = UNSET
    load_match_command: Union[Unset, str] = UNSET
    server: Union[Unset, 'Server'] = UNSET
    guild: Union[Unset, 'Guild'] = UNSET
    status: Union[Unset, StatusEnum] = UNSET
    type: Union[Unset, TypeEnum] = UNSET
    num_maps: Union[Unset, int] = UNSET
    maplist: Union[Unset, Any] = UNSET
    map_sides: Union[Unset, Any] = UNSET
    clinch_series: Union[Unset, bool] = UNSET
    cvars: Union[Unset, Any] = UNSET
    players_per_team: Union[Unset, int] = UNSET
    message_id: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    winner_team: Union[None, Unset, str] = UNSET
    author: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.team import Team
        from ..models.guild import Guild
        from ..models.map_ban import MapBan
        from ..models.server import Server
        from ..models.match_map_selected import MatchMapSelected
        from ..models.map_ import Map
        id = self.id

        team1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team1, Unset):
            team1 = self.team1.to_dict()

        team2: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team2, Unset):
            team2 = self.team2.to_dict()

        maps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.maps, Unset):
            maps = []
            for maps_item_data in self.maps:
                maps_item = maps_item_data.to_dict()
                maps.append(maps_item)





        map_bans: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.map_bans, Unset):
            map_bans = []
            for map_bans_item_data in self.map_bans:
                map_bans_item = map_bans_item_data.to_dict()
                map_bans.append(map_bans_item)





        map_picks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.map_picks, Unset):
            map_picks = []
            for map_picks_item_data in self.map_picks:
                map_picks_item = map_picks_item_data.to_dict()
                map_picks.append(map_picks_item)





        connect_command = self.connect_command

        load_match_command = self.load_match_command

        server: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        guild: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.guild, Unset):
            guild = self.guild.to_dict()

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

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        winner_team: Union[None, Unset, str]
        if isinstance(self.winner_team, Unset):
            winner_team = UNSET
        else:
            winner_team = self.winner_team

        author: Union[None, Unset, str]
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if team1 is not UNSET:
            field_dict["team1"] = team1
        if team2 is not UNSET:
            field_dict["team2"] = team2
        if maps is not UNSET:
            field_dict["maps"] = maps
        if map_bans is not UNSET:
            field_dict["map_bans"] = map_bans
        if map_picks is not UNSET:
            field_dict["map_picks"] = map_picks
        if connect_command is not UNSET:
            field_dict["connect_command"] = connect_command
        if load_match_command is not UNSET:
            field_dict["load_match_command"] = load_match_command
        if server is not UNSET:
            field_dict["server"] = server
        if guild is not UNSET:
            field_dict["guild"] = guild
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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if winner_team is not UNSET:
            field_dict["winner_team"] = winner_team
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team import Team
        from ..models.guild import Guild
        from ..models.map_ban import MapBan
        from ..models.server import Server
        from ..models.match_map_selected import MatchMapSelected
        from ..models.map_ import Map
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _team1 = d.pop("team1", UNSET)
        team1: Union[Unset, Team]
        if isinstance(_team1,  Unset):
            team1 = UNSET
        else:
            team1 = Team.from_dict(_team1)




        _team2 = d.pop("team2", UNSET)
        team2: Union[Unset, Team]
        if isinstance(_team2,  Unset):
            team2 = UNSET
        else:
            team2 = Team.from_dict(_team2)




        maps = []
        _maps = d.pop("maps", UNSET)
        for maps_item_data in (_maps or []):
            maps_item = Map.from_dict(maps_item_data)



            maps.append(maps_item)


        map_bans = []
        _map_bans = d.pop("map_bans", UNSET)
        for map_bans_item_data in (_map_bans or []):
            map_bans_item = MapBan.from_dict(map_bans_item_data)



            map_bans.append(map_bans_item)


        map_picks = []
        _map_picks = d.pop("map_picks", UNSET)
        for map_picks_item_data in (_map_picks or []):
            map_picks_item = MatchMapSelected.from_dict(map_picks_item_data)



            map_picks.append(map_picks_item)


        connect_command = d.pop("connect_command", UNSET)

        load_match_command = d.pop("load_match_command", UNSET)

        _server = d.pop("server", UNSET)
        server: Union[Unset, Server]
        if isinstance(_server,  Unset):
            server = UNSET
        else:
            server = Server.from_dict(_server)




        _guild = d.pop("guild", UNSET)
        guild: Union[Unset, Guild]
        if isinstance(_guild,  Unset):
            guild = UNSET
        else:
            guild = Guild.from_dict(_guild)




        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusEnum]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = StatusEnum(_status)




        _type = d.pop("type", UNSET)
        type: Union[Unset, TypeEnum]
        if isinstance(_type,  Unset):
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


        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        def _parse_winner_team(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        winner_team = _parse_winner_team(d.pop("winner_team", UNSET))


        def _parse_author(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        author = _parse_author(d.pop("author", UNSET))


        patched_match = cls(
            id=id,
            team1=team1,
            team2=team2,
            maps=maps,
            map_bans=map_bans,
            map_picks=map_picks,
            connect_command=connect_command,
            load_match_command=load_match_command,
            server=server,
            guild=guild,
            status=status,
            type=type,
            num_maps=num_maps,
            maplist=maplist,
            map_sides=map_sides,
            clinch_series=clinch_series,
            cvars=cvars,
            players_per_team=players_per_team,
            message_id=message_id,
            created_at=created_at,
            updated_at=updated_at,
            winner_team=winner_team,
            author=author,
        )

        patched_match.additional_properties = d
        return patched_match

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
