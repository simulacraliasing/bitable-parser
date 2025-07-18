from lark_oapi.core.construct import init as init

class AuditLogNetInfo:
    client_ip: str | None
    ip_loc: str | None
    ip_provider: str | None
    referer: str | None
    origin: str | None
    user_agent: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AuditLogNetInfoBuilder: ...

class AuditLogNetInfoBuilder:
    def __init__(self) -> None: ...
    def client_ip(self, client_ip: str) -> AuditLogNetInfoBuilder: ...
    def ip_loc(self, ip_loc: str) -> AuditLogNetInfoBuilder: ...
    def ip_provider(self, ip_provider: str) -> AuditLogNetInfoBuilder: ...
    def referer(self, referer: str) -> AuditLogNetInfoBuilder: ...
    def origin(self, origin: str) -> AuditLogNetInfoBuilder: ...
    def user_agent(self, user_agent: str) -> AuditLogNetInfoBuilder: ...
    def build(self) -> AuditLogNetInfo: ...
