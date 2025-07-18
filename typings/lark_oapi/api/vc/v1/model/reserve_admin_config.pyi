from .subscribe_department import SubscribeDepartment as SubscribeDepartment
from .subscribe_user import SubscribeUser as SubscribeUser
from lark_oapi.core.construct import init as init

class ReserveAdminConfig:
    depts: list[SubscribeDepartment] | None
    users: list[SubscribeUser] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ReserveAdminConfigBuilder: ...

class ReserveAdminConfigBuilder:
    def __init__(self) -> None: ...
    def depts(self, depts: list[SubscribeDepartment]) -> ReserveAdminConfigBuilder: ...
    def users(self, users: list[SubscribeUser]) -> ReserveAdminConfigBuilder: ...
    def build(self) -> ReserveAdminConfig: ...
