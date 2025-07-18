from lark_oapi.core.construct import init as init

class CreateOidcAccessTokenResponseBody:
    access_token: str | None
    refresh_token: str | None
    token_type: str | None
    expires_in: int | None
    refresh_expires_in: int | None
    scope: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateOidcAccessTokenResponseBodyBuilder: ...

class CreateOidcAccessTokenResponseBodyBuilder:
    def __init__(self) -> None: ...
    def access_token(self, access_token: str) -> CreateOidcAccessTokenResponseBodyBuilder: ...
    def refresh_token(self, refresh_token: str) -> CreateOidcAccessTokenResponseBodyBuilder: ...
    def token_type(self, token_type: str) -> CreateOidcAccessTokenResponseBodyBuilder: ...
    def expires_in(self, expires_in: int) -> CreateOidcAccessTokenResponseBodyBuilder: ...
    def refresh_expires_in(self, refresh_expires_in: int) -> CreateOidcAccessTokenResponseBodyBuilder: ...
    def scope(self, scope: str) -> CreateOidcAccessTokenResponseBodyBuilder: ...
    def build(self) -> CreateOidcAccessTokenResponseBody: ...
