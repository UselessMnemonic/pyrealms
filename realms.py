import requests


class RealmsResponse:
    def __init__(self, data: dict):
        self.error_code = data.get('errorCode', None)
        self.error_message = data.get('errorMsg', None)


class Server:
    def __init__(self, data: dict):
        id = data['id']
        remote_subscription_id = data['remoteSubscriptionId']
        owner = data['owner']
        owner_uuid = data['ownerUUID']
        name = data['name']
        motd = data['motd']
        state = data['state']
        days_left = data['daysLeft']
        expired = data['expired']
        expired_trial = data['expiredTrial']
        world_type = data['worldType']
        players = data['players']
        max_players = data['maxPlayers']
        minigame_name = data['minigameName']
        minigame_id = data['minigameId']
        minigame_image = data['minigameImage']
        active_slot = data['activeSlot']


class Backup:
    def __init__(self, data: dict):
        backup_id = data['backupId']
        last_modified_date = data['lastModifiedDate']
        size = data['size']
        metadata = data['metadata']
        game_difficulty = metadata['game_difficulty']
        name = metadata['name']
        game_server_version = metadata['game_server_version']
        packs = metadata['enabled_packs']
        resource_packs = packs['resourcePacks']
        behaviour_packs = packs['behaviorPacks']
        description = metadata['description']
        game_mode = metadata['game_mode']
        world_type = metadata['world_type']


class RealmsSession(requests.Session):
    def __init__(self, access_token, user, uuid, version):
        super().__init__()
        self.cookies.set("sid", f"token:{access_token}:{uuid}")
        self.cookies.set("user", user)
        self.cookies.set("version", version)
        self.headers.update({
            "Connection": "close",
            "Content-Type": "application/json",
            "Host": "pc.realms.minecraft.net",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache"
        })


class RealmsRequest(requests.Request):
    def __init__(self, method, endpoint):
        super().__init__(method, f"https://pc.realms.minecraft.net/{endpoint}")

    def send(self, session):
        return RealmsResponse(session.send(session.prepare_request(self)).json())


class GetWorldsRequest(RealmsRequest):
    def __init__(self):
        super().__init__("GET", "worlds")

    def send(self, session):
        return GetWorldsResponse(session.send(session.prepare_request(self)).json())


class GetWorldsResponse(RealmsResponse):
    def __init__(self, data: dict):
        super().__init__(data)
        self.servers = []
        if not self.error_code:
            for s in data['servers']:
                self.servers.append(Server(s))


class GetWorldRequest(RealmsRequest):
    def __init__(self, world_id):
        super().__init__("GET", f"worlds/{world_id}")

    def send(self, session):
        return GetWorldResponse(session.send(session.prepare_request(self)).json())


class GetWorldResponse(RealmsResponse):
    def __init__(self, data: dict):
        super().__init__(data)
        self.server = None
        if not self.error_code:
            self.server = Server(data)


class GetWorldBackupsRequest(RealmsRequest):
    def __init__(self, world_id):
        super().__init__("GET", f"worlds/{world_id}")

    def send(self, session):
        return GetWorldBackupsResponse(session.send(session.prepare_request(self)).json())


class GetWorldBackupsResponse(RealmsResponse):
    def __init__(self, data: dict):
        super().__init__(data)
        self.backup = None
        if not self.error_code:
            self.backup = Backup(data)
