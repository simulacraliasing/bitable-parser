from .tasklist import Tasklist as Tasklist
from lark_oapi.core.construct import init as init

class AddMembersTasklistResponseBody:
    tasklist: Tasklist | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AddMembersTasklistResponseBodyBuilder: ...

class AddMembersTasklistResponseBodyBuilder:
    def __init__(self) -> None: ...
    def tasklist(self, tasklist: Tasklist) -> AddMembersTasklistResponseBodyBuilder: ...
    def build(self) -> AddMembersTasklistResponseBody: ...
