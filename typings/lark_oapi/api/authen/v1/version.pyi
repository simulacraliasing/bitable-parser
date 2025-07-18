from .resource import *

class V1:
    access_token: AccessToken
    oidc_access_token: OidcAccessToken
    oidc_refresh_access_token: OidcRefreshAccessToken
    refresh_access_token: RefreshAccessToken
    user_info: UserInfo
    def __init__(self, config: Config) -> None: ...
