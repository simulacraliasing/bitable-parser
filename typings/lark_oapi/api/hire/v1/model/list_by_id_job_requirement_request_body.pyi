from lark_oapi.core.construct import init as init

class ListByIdJobRequirementRequestBody:
    id_list: list[str] | None
    short_code_list: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListByIdJobRequirementRequestBodyBuilder: ...

class ListByIdJobRequirementRequestBodyBuilder:
    def __init__(self) -> None: ...
    def id_list(self, id_list: list[str]) -> ListByIdJobRequirementRequestBodyBuilder: ...
    def short_code_list(self, short_code_list: list[str]) -> ListByIdJobRequirementRequestBodyBuilder: ...
    def build(self) -> ListByIdJobRequirementRequestBody: ...
