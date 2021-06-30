from typing import Optional

import requests

class Profile:
    def __init__(self, data: dict): ...
    name: str
    id: str


class AccessTokenResponse:
    def __init__(self, data: dict): ...
    error: str
    error_message: str
    client_token: str
    access_token: str
    selected_profile: Optional[Profile]
    available_profiles: [Profile]


class AccessTokenRequest(requests.Request):
    def __init__(self, username: str, password: str, token: str): ...
    def send(self) -> AccessTokenResponse: ...


def request_access_token(username, password, token) -> str: ...