from lark_oapi.core.construct import init as init

class ExchangeBinding:
    admin_account: str | None
    exchange_account: str | None
    user_id: str | None
    status: str | None
    exchange_binding_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ExchangeBindingBuilder: ...

class ExchangeBindingBuilder:
    def __init__(self) -> None: ...
    def admin_account(self, admin_account: str) -> ExchangeBindingBuilder: ...
    def exchange_account(self, exchange_account: str) -> ExchangeBindingBuilder: ...
    def user_id(self, user_id: str) -> ExchangeBindingBuilder: ...
    def status(self, status: str) -> ExchangeBindingBuilder: ...
    def exchange_binding_id(self, exchange_binding_id: str) -> ExchangeBindingBuilder: ...
    def build(self) -> ExchangeBinding: ...
