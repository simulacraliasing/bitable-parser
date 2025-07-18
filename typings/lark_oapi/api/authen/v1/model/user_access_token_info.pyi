from lark_oapi.core.construct import init as init

class UserAccessTokenInfo:
    access_token: str | None
    token_type: str | None
    expires_in: int | None
    name: str | None
    en_name: str | None
    avatar_url: str | None
    avatar_thumb: str | None
    avatar_middle: str | None
    avatar_big: str | None
    open_id: str | None
    union_id: str | None
    email: str | None
    enterprise_email: str | None
    user_id: str | None
    mobile: str | None
    tenant_key: str | None
    refresh_expires_in: int | None
    refresh_token: str | None
    sid: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UserAccessTokenInfoBuilder: ...

class UserAccessTokenInfoBuilder:
    def __init__(self) -> None: ...
    def access_token(self, access_token: str) -> UserAccessTokenInfoBuilder: ...
    def token_type(self, token_type: str) -> UserAccessTokenInfoBuilder: ...
    def expires_in(self, expires_in: int) -> UserAccessTokenInfoBuilder: ...
    def name(self, name: str) -> UserAccessTokenInfoBuilder: ...
    def en_name(self, en_name: str) -> UserAccessTokenInfoBuilder: ...
    def avatar_url(self, avatar_url: str) -> UserAccessTokenInfoBuilder: ...
    def avatar_thumb(self, avatar_thumb: str) -> UserAccessTokenInfoBuilder: ...
    def avatar_middle(self, avatar_middle: str) -> UserAccessTokenInfoBuilder: ...
    def avatar_big(self, avatar_big: str) -> UserAccessTokenInfoBuilder: ...
    def open_id(self, open_id: str) -> UserAccessTokenInfoBuilder: ...
    def union_id(self, union_id: str) -> UserAccessTokenInfoBuilder: ...
    def email(self, email: str) -> UserAccessTokenInfoBuilder: ...
    def enterprise_email(self, enterprise_email: str) -> UserAccessTokenInfoBuilder: ...
    def user_id(self, user_id: str) -> UserAccessTokenInfoBuilder: ...
    def mobile(self, mobile: str) -> UserAccessTokenInfoBuilder: ...
    def tenant_key(self, tenant_key: str) -> UserAccessTokenInfoBuilder: ...
    def refresh_expires_in(self, refresh_expires_in: int) -> UserAccessTokenInfoBuilder: ...
    def refresh_token(self, refresh_token: str) -> UserAccessTokenInfoBuilder: ...
    def sid(self, sid: str) -> UserAccessTokenInfoBuilder: ...
    def build(self) -> UserAccessTokenInfo: ...
