from .person_info import PersonInfo as PersonInfo
from lark_oapi.core.construct import init as init

class CreatePersonResponseBody:
    person: PersonInfo | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreatePersonResponseBodyBuilder: ...

class CreatePersonResponseBodyBuilder:
    def __init__(self) -> None: ...
    def person(self, person: PersonInfo) -> CreatePersonResponseBodyBuilder: ...
    def build(self) -> CreatePersonResponseBody: ...
