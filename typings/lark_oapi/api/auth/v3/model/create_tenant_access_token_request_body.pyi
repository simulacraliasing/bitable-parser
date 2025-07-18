from lark_oapi.core.construct import init as init

class CreateTenantAccessTokenRequestBody:
    app_access_token: str | None
    tenant_key: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateTenantAccessTokenRequestBodyBuilder: ...

class CreateTenantAccessTokenRequestBodyBuilder:
    def __init__(self) -> None: ...
    def app_access_token(self, app_access_token: str) -> CreateTenantAccessTokenRequestBodyBuilder: ...
    def tenant_key(self, tenant_key: str) -> CreateTenantAccessTokenRequestBodyBuilder: ...
    def build(self) -> CreateTenantAccessTokenRequestBody: ...
