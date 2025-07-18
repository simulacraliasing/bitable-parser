from lark_oapi.core.construct import init as init

class AppTableForm:
    name: str | None
    description: str | None
    shared: bool | None
    shared_url: str | None
    shared_limit: str | None
    submit_limit_once: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AppTableFormBuilder: ...

class AppTableFormBuilder:
    def __init__(self) -> None: ...
    def name(self, name: str) -> AppTableFormBuilder: ...
    def description(self, description: str) -> AppTableFormBuilder: ...
    def shared(self, shared: bool) -> AppTableFormBuilder: ...
    def shared_url(self, shared_url: str) -> AppTableFormBuilder: ...
    def shared_limit(self, shared_limit: str) -> AppTableFormBuilder: ...
    def submit_limit_once(self, submit_limit_once: bool) -> AppTableFormBuilder: ...
    def build(self) -> AppTableForm: ...
