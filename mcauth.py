import json
import requests


class Profile:
    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']


class AccessTokenResponse:
    def __init__(self, data):
        super().__init__()
        self.error = data.get('error', None)
        self.error_message = data.get('errorMessage', None)
        self.client_token = data.get('clientToken', None)
        self.access_token = data.get('accessToken', None)
        self.selected_profile = None
        if 'selectedProfile' in data:
            self.selected_profile = Profile(data['selectedProfile'])
        self.available_profiles = []
        if 'availableProfiles' in data:
            for p in data['availableProfiles']:
                self.available_profiles.append(Profile(p))


class AccessTokenRequest(requests.Request):
    def __init__(self, username, password, token):
        super().__init__(method="POST", url="https://authserver.mojang.com/authenticate", headers={
            "Accept": "application/json",
            "Connection": "close",
            "Content-Type": "application/json",
            "Host": "authserver.mojang.com"
        })
        self.data = json.dumps({
            "agent": {
                "name": "Minecraft",
                "version": 1
            },
            "username": username,
            "password": password,
            "clientToken": token
        })

    def send(self):
        return AccessTokenResponse(requests.Session().send(self.prepare()).json())


def request_access_token(username, password, token):
    return AccessTokenRequest(username, password, token).send().access_token
