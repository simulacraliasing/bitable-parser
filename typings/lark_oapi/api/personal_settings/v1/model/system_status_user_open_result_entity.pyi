from lark_oapi.core.construct import init as init

class SystemStatusUserOpenResultEntity:
    user_id: str | None
    end_time: str | None
    result: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SystemStatusUserOpenResultEntityBuilder: ...

class SystemStatusUserOpenResultEntityBuilder:
    def __init__(self) -> None: ...
    def user_id(self, user_id: str) -> SystemStatusUserOpenResultEntityBuilder: ...
    def end_time(self, end_time: str) -> SystemStatusUserOpenResultEntityBuilder: ...
    def result(self, result: str) -> SystemStatusUserOpenResultEntityBuilder: ...
    def build(self) -> SystemStatusUserOpenResultEntity: ...
