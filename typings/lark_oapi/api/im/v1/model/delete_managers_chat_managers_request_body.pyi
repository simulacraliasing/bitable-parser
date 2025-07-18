from lark_oapi.core.construct import init as init

class DeleteManagersChatManagersRequestBody:
    manager_ids: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteManagersChatManagersRequestBodyBuilder: ...

class DeleteManagersChatManagersRequestBodyBuilder:
    def __init__(self) -> None: ...
    def manager_ids(self, manager_ids: list[str]) -> DeleteManagersChatManagersRequestBodyBuilder: ...
    def build(self) -> DeleteManagersChatManagersRequestBody: ...
