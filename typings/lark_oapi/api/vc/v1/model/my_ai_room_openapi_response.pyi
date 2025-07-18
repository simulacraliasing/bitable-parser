from lark_oapi.core.construct import init as init

class MyAiRoomOpenapiResponse:
    response_type: int | None
    schedule_event_id: str | None
    other_msg: str | None
    oapi_msg: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MyAiRoomOpenapiResponseBuilder: ...

class MyAiRoomOpenapiResponseBuilder:
    def __init__(self) -> None: ...
    def response_type(self, response_type: int) -> MyAiRoomOpenapiResponseBuilder: ...
    def schedule_event_id(self, schedule_event_id: str) -> MyAiRoomOpenapiResponseBuilder: ...
    def other_msg(self, other_msg: str) -> MyAiRoomOpenapiResponseBuilder: ...
    def oapi_msg(self, oapi_msg: str) -> MyAiRoomOpenapiResponseBuilder: ...
    def build(self) -> MyAiRoomOpenapiResponse: ...
