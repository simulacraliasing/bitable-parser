from .resource import *

class V3:
    app_access_token: AppAccessToken
    app_ticket: AppTicket
    tenant_access_token: TenantAccessToken
    def __init__(self, config: Config) -> None: ...
