from typing import Optional

import requests


class Server:
    def __init__(self, data: dict): ...
    id: int
    remote_subscription_id: str
    owner: str
    owner_uuid: str
    name: str
    motd: str
    state: str
    days_left: int
    expired: bool
    expired_trial: bool
    world_type: str
    players: [str]
    max_players: int
    minigame_name: str
    minigame_id: int
    minigame_image: str
    active_slot: int


class Backup:
    def __init__(self, data: dict): ...
    backup_id: int
    last_modified_date: str
    size: int
    game_difficulty: str
    name: str
    game_server_version: str
    resource_packs: [str]
    behaviour_packs: [str]
    description: str
    game_mode: str
    world_type: str


class RealmsSession(requests.Session):
    def __init__(self, access_token: str, user: str, uuid: str, version: str): ...


class RealmsRequest(requests.Request):
    def __init__(self, method: str, endpoint: str): ...
    def send(self, session: RealmsSession) -> dict: ...


class RealmsResponse:
    def __init__(self, data: dict): ...
    error_code: Optional[int]
    error_message: str


class GetWorldsRequest(RealmsRequest):
    def __init__(self): ...
    def send(self, session: RealmsSession) -> GetWorldsResponse: ...


class GetWorldsResponse(RealmsResponse):
    def __init__(self, data: dict): ...
    servers: [Server]


class GetWorldRequest(RealmsRequest):
    def __init__(self, world_id: int): ...
    def send(self, session: RealmsSession) -> GetWorldResponse: ...


class GetWorldResponse(RealmsResponse):
    def __init__(self, data: dict): ...
    server: Optional[Server]


class GetWorldBackupsRequest(RealmsRequest):
    def __init__(self, world_id: int): ...
    def send(self, session: RealmsSession) -> GetWorldBackupsResponse: ...


class GetWorldBackupsResponse(RealmsResponse):
    def __init__(self, data: dict): ...
    backup: Optional[Backup]
