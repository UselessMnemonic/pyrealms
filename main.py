import mcauth
import realms

if __name__ == '__main__':
    auth_request = mcauth.AccessTokenRequest("TODO", "TODO", "any-constant-string")
    auth_response = auth_request.send()
    if not auth_response.error:
        print(auth_response)
        access_token = auth_response.access_token
        profile = auth_response.selected_profile
        name = profile.name
        uuid = profile.id
        rs = realms.RealmsSession(access_token, name, uuid, "1.17.0")

        res = realms.GetWorldRequest(9193751).send(rs)
        print(res.server.players)

