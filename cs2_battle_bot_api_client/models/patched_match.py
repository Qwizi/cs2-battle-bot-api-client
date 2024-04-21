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
    from ..models.match_map_selected import MatchMapSelected
    from ..models.patched_match_config import PatchedMatchConfig
    from ..models.server import Server
    from ..models.team import Team


T = TypeVar("T", bound="PatchedMatch")


@_attrs_define
class PatchedMatch:
    """
    Attributes:
        id (Union[Unset, int]):
        team1 (Union[Unset, Team]):
        team2 (Union[Unset, Team]):
        maps (Union[Unset, List['Map']]):
        winner_team (Union['Team', None, Unset]):
        map_bans (Union[Unset, List['MapBan']]):
        last_map_ban (Union['MapBan', None, Unset]):
        map_picks (Union[Unset, List['MatchMapSelected']]):
        last_map_pick (Union['MatchMapSelected', None, Unset]):
        author (Union[Unset, DiscordUser]):
        server (Union['Server', None, Unset]):
        guild (Union[Unset, Guild]):
        config_url (Union[Unset, str]):
        config (Union[Unset, PatchedMatchConfig]):
        webhook_url (Union[Unset, str]):
        connect_command (Union[Unset, str]):
        load_match_command (Union[Unset, str]):
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
    """

    id: Union[Unset, int] = UNSET
    team1: Union[Unset, "Team"] = UNSET
    team2: Union[Unset, "Team"] = UNSET
    maps: Union[Unset, List["Map"]] = UNSET
    winner_team: Union["Team", None, Unset] = UNSET
    map_bans: Union[Unset, List["MapBan"]] = UNSET
    last_map_ban: Union["MapBan", None, Unset] = UNSET
    map_picks: Union[Unset, List["MatchMapSelected"]] = UNSET
    last_map_pick: Union["MatchMapSelected", None, Unset] = UNSET
    author: Union[Unset, "DiscordUser"] = UNSET
    server: Union["Server", None, Unset] = UNSET
    guild: Union[Unset, "Guild"] = UNSET
    config_url: Union[Unset, str] = UNSET
    config: Union[Unset, "PatchedMatchConfig"] = UNSET
    webhook_url: Union[Unset, str] = UNSET
    connect_command: Union[Unset, str] = UNSET
    load_match_command: Union[Unset, str] = UNSET
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
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.map_ban import MapBan
        from ..models.match_map_selected import MatchMapSelected
        from ..models.server import Server
        from ..models.team import Team

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

        winner_team: Union[Dict[str, Any], None, Unset]
        if isinstance(self.winner_team, Unset):
            winner_team = UNSET
        elif isinstance(self.winner_team, Team):
            winner_team = self.winner_team.to_dict()
        else:
            winner_team = self.winner_team

        map_bans: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.map_bans, Unset):
            map_bans = []
            for map_bans_item_data in self.map_bans:
                map_bans_item = map_bans_item_data.to_dict()
                map_bans.append(map_bans_item)

        last_map_ban: Union[Dict[str, Any], None, Unset]
        if isinstance(self.last_map_ban, Unset):
            last_map_ban = UNSET
        elif isinstance(self.last_map_ban, MapBan):
            last_map_ban = self.last_map_ban.to_dict()
        else:
            last_map_ban = self.last_map_ban

        map_picks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.map_picks, Unset):
            map_picks = []
            for map_picks_item_data in self.map_picks:
                map_picks_item = map_picks_item_data.to_dict()
                map_picks.append(map_picks_item)

        last_map_pick: Union[Dict[str, Any], None, Unset]
        if isinstance(self.last_map_pick, Unset):
            last_map_pick = UNSET
        elif isinstance(self.last_map_pick, MatchMapSelected):
            last_map_pick = self.last_map_pick.to_dict()
        else:
            last_map_pick = self.last_map_pick

        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        server: Union[Dict[str, Any], None, Unset]
        if isinstance(self.server, Unset):
            server = UNSET
        elif isinstance(self.server, Server):
            server = self.server.to_dict()
        else:
            server = self.server

        guild: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.guild, Unset):
            guild = self.guild.to_dict()

        config_url = self.config_url

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        webhook_url = self.webhook_url

        connect_command = self.connect_command

        load_match_command = self.load_match_command

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if team1 is not UNSET:
            field_dict["team1"] = team1
        if team2 is not UNSET:
            field_dict["team2"] = team2
        if maps is not UNSET:
            field_dict["maps"] = maps
        if winner_team is not UNSET:
            field_dict["winner_team"] = winner_team
        if map_bans is not UNSET:
            field_dict["map_bans"] = map_bans
        if last_map_ban is not UNSET:
            field_dict["last_map_ban"] = last_map_ban
        if map_picks is not UNSET:
            field_dict["map_picks"] = map_picks
        if last_map_pick is not UNSET:
            field_dict["last_map_pick"] = last_map_pick
        if author is not UNSET:
            field_dict["author"] = author
        if server is not UNSET:
            field_dict["server"] = server
        if guild is not UNSET:
            field_dict["guild"] = guild
        if config_url is not UNSET:
            field_dict["config_url"] = config_url
        if config is not UNSET:
            field_dict["config"] = config
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url
        if connect_command is not UNSET:
            field_dict["connect_command"] = connect_command
        if load_match_command is not UNSET:
            field_dict["load_match_command"] = load_match_command
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.discord_user import DiscordUser
        from ..models.guild import Guild
        from ..models.map_ import Map
        from ..models.map_ban import MapBan
        from ..models.match_map_selected import MatchMapSelected
        from ..models.patched_match_config import PatchedMatchConfig
        from ..models.server import Server
        from ..models.team import Team

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _team1 = d.pop("team1", UNSET)
        team1: Union[Unset, Team]
        if isinstance(_team1, Unset):
            team1 = UNSET
        else:
            team1 = Team.from_dict(_team1)

        _team2 = d.pop("team2", UNSET)
        team2: Union[Unset, Team]
        if isinstance(_team2, Unset):
            team2 = UNSET
        else:
            team2 = Team.from_dict(_team2)

        maps = []
        _maps = d.pop("maps", UNSET)
        for maps_item_data in _maps or []:
            maps_item = Map.from_dict(maps_item_data)

            maps.append(maps_item)

        def _parse_winner_team(data: object) -> Union["Team", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                winner_team_type_1 = Team.from_dict(data)

                return winner_team_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Team", None, Unset], data)

        winner_team = _parse_winner_team(d.pop("winner_team", UNSET))

        map_bans = []
        _map_bans = d.pop("map_bans", UNSET)
        for map_bans_item_data in _map_bans or []:
            map_bans_item = MapBan.from_dict(map_bans_item_data)

            map_bans.append(map_bans_item)

        def _parse_last_map_ban(data: object) -> Union["MapBan", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_map_ban_type_1 = MapBan.from_dict(data)

                return last_map_ban_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MapBan", None, Unset], data)

        last_map_ban = _parse_last_map_ban(d.pop("last_map_ban", UNSET))

        map_picks = []
        _map_picks = d.pop("map_picks", UNSET)
        for map_picks_item_data in _map_picks or []:
            map_picks_item = MatchMapSelected.from_dict(map_picks_item_data)

            map_picks.append(map_picks_item)

        def _parse_last_map_pick(data: object) -> Union["MatchMapSelected", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_map_pick_type_1 = MatchMapSelected.from_dict(data)

                return last_map_pick_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchMapSelected", None, Unset], data)

        last_map_pick = _parse_last_map_pick(d.pop("last_map_pick", UNSET))

        _author = d.pop("author", UNSET)
        author: Union[Unset, DiscordUser]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = DiscordUser.from_dict(_author)

        def _parse_server(data: object) -> Union["Server", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                server_type_1 = Server.from_dict(data)

                return server_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Server", None, Unset], data)

        server = _parse_server(d.pop("server", UNSET))

        _guild = d.pop("guild", UNSET)
        guild: Union[Unset, Guild]
        if isinstance(_guild, Unset):
            guild = UNSET
        else:
            guild = Guild.from_dict(_guild)

        config_url = d.pop("config_url", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, PatchedMatchConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = PatchedMatchConfig.from_dict(_config)

        webhook_url = d.pop("webhook_url", UNSET)

        connect_command = d.pop("connect_command", UNSET)

        load_match_command = d.pop("load_match_command", UNSET)

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

        patched_match = cls(
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
