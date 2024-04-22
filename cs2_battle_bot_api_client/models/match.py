import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.status_enum import StatusEnum
from ..models.type_enum import TypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discord_user import DiscordUser
    from ..models.guild import Guild
    from ..models.map_ import Map
    from ..models.map_ban import MapBan
    from ..models.match_config import MatchConfig
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
        maps (List['Map']):
        winner_team (Union['Team', None]):
        map_bans (List['MapBan']):
        last_map_ban (Union['MapBan', None]):
        map_picks (List['MatchMapSelected']):
        last_map_pick (Union['MatchMapSelected', None]):
        author (DiscordUser):
        server (Union['Server', None]):
        guild (Guild):
        config_url (str):
        config (MatchConfig):
        webhook_url (str):
        connect_command (str):
        load_match_command (str):
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
    """

    id: int
    team1: "Team"
    team2: "Team"
    maps: List["Map"]
    winner_team: Union["Team", None]
    map_bans: List["MapBan"]
    last_map_ban: Union["MapBan", None]
    map_picks: List["MatchMapSelected"]
    last_map_pick: Union["MatchMapSelected", None]
    author: "DiscordUser"
    server: Union["Server", None]
    guild: "Guild"
    config_url: str
    config: "MatchConfig"
    webhook_url: str
    connect_command: str
    load_match_command: str
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
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.map_ban import MapBan
        from ..models.match_map_selected import MatchMapSelected
        from ..models.server import Server
        from ..models.team import Team

        id = self.id

        team1 = self.team1.to_dict()

        team2 = self.team2.to_dict()

        maps = []
        for maps_item_data in self.maps:
            maps_item = maps_item_data.to_dict()
            maps.append(maps_item)

        winner_team: Union[Dict[str, Any], None]
        if isinstance(self.winner_team, Team):
            winner_team = self.winner_team.to_dict()
        else:
            winner_team = self.winner_team

        map_bans = []
        for map_bans_item_data in self.map_bans:
            map_bans_item = map_bans_item_data.to_dict()
            map_bans.append(map_bans_item)

        last_map_ban: Union[Dict[str, Any], None]
        if isinstance(self.last_map_ban, MapBan):
            last_map_ban = self.last_map_ban.to_dict()
        else:
            last_map_ban = self.last_map_ban

        map_picks = []
        for map_picks_item_data in self.map_picks:
            map_picks_item = map_picks_item_data.to_dict()
            map_picks.append(map_picks_item)

        last_map_pick: Union[Dict[str, Any], None]
        if isinstance(self.last_map_pick, MatchMapSelected):
            last_map_pick = self.last_map_pick.to_dict()
        else:
            last_map_pick = self.last_map_pick

        author = self.author.to_dict()

        server: Union[Dict[str, Any], None]
        if isinstance(self.server, Server):
            server = self.server.to_dict()
        else:
            server = self.server

        guild = self.guild.to_dict()

        config_url = self.config_url

        config = self.config.to_dict()

        webhook_url = self.webhook_url

        connect_command = self.connect_command

        load_match_command = self.load_match_command

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "team1": team1,
                "team2": team2,
                "maps": maps,
                "winner_team": winner_team,
                "map_bans": map_bans,
                "last_map_ban": last_map_ban,
                "map_picks": map_picks,
                "last_map_pick": last_map_pick,
                "author": author,
                "server": server,
                "guild": guild,
                "config_url": config_url,
                "config": config,
                "webhook_url": webhook_url,
                "connect_command": connect_command,
                "load_match_command": load_match_command,
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.discord_user import DiscordUser
        from ..models.guild import Guild
        from ..models.map_ import Map
        from ..models.map_ban import MapBan
        from ..models.match_config import MatchConfig
        from ..models.match_map_selected import MatchMapSelected
        from ..models.server import Server
        from ..models.team import Team

        d = src_dict.copy()
        id = d.pop("id")

        team1 = Team.from_dict(d.pop("team1"))

        team2 = Team.from_dict(d.pop("team2"))

        maps = []
        _maps = d.pop("maps")
        for maps_item_data in _maps:
            maps_item = Map.from_dict(maps_item_data)

            maps.append(maps_item)

        def _parse_winner_team(data: object) -> Union["Team", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                winner_team_type_1 = Team.from_dict(data)

                return winner_team_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Team", None], data)

        winner_team = _parse_winner_team(d.pop("winner_team"))

        map_bans = []
        _map_bans = d.pop("map_bans")
        for map_bans_item_data in _map_bans:
            map_bans_item = MapBan.from_dict(map_bans_item_data)

            map_bans.append(map_bans_item)

        def _parse_last_map_ban(data: object) -> Union["MapBan", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_map_ban_type_1 = MapBan.from_dict(data)

                return last_map_ban_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MapBan", None], data)

        last_map_ban = _parse_last_map_ban(d.pop("last_map_ban"))

        map_picks = []
        _map_picks = d.pop("map_picks")
        for map_picks_item_data in _map_picks:
            map_picks_item = MatchMapSelected.from_dict(map_picks_item_data)

            map_picks.append(map_picks_item)

        def _parse_last_map_pick(data: object) -> Union["MatchMapSelected", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_map_pick_type_1 = MatchMapSelected.from_dict(data)

                return last_map_pick_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchMapSelected", None], data)

        last_map_pick = _parse_last_map_pick(d.pop("last_map_pick"))

        author = DiscordUser.from_dict(d.pop("author"))

        def _parse_server(data: object) -> Union["Server", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                server_type_1 = Server.from_dict(data)

                return server_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Server", None], data)

        server = _parse_server(d.pop("server"))

        guild = Guild.from_dict(d.pop("guild"))

        config_url = d.pop("config_url")

        config = MatchConfig.from_dict(d.pop("config"))

        webhook_url = d.pop("webhook_url")

        connect_command = d.pop("connect_command")

        load_match_command = d.pop("load_match_command")

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

        match = cls(
            id=id,
            team1=team1,
            team2=team2,
            maps=maps,
            winner_team=winner_team,
            map_bans=map_bans,
            last_map_ban=last_map_ban,
            map_picks=map_picks,
            last_map_pick=last_map_pick,
            author=author,
            server=server,
            guild=guild,
            config_url=config_url,
            config=config,
            webhook_url=webhook_url,
            connect_command=connect_command,
            load_match_command=load_match_command,
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
