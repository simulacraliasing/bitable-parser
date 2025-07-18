from .my_ai_room_openapi_response import MyAiRoomOpenapiResponse as MyAiRoomOpenapiResponse
from lark_oapi.core.construct import init as init

class MyAiVcRoomRequestCommonParam:
    language: str | None
    utc_offset: str | None
    room_id: str | None
    client_version: str | None
    openapi_history: MyAiRoomOpenapiResponse | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MyAiVcRoomRequestCommonParamBuilder: ...

class MyAiVcRoomRequestCommonParamBuilder:
    def __init__(self) -> None: ...
    def language(self, language: str) -> MyAiVcRoomRequestCommonParamBuilder: ...
    def utc_offset(self, utc_offset: str) -> MyAiVcRoomRequestCommonParamBuilder: ...
    def room_id(self, room_id: str) -> MyAiVcRoomRequestCommonParamBuilder: ...
    def client_version(self, client_version: str) -> MyAiVcRoomRequestCommonParamBuilder: ...
    def openapi_history(self, openapi_history: MyAiRoomOpenapiResponse) -> MyAiVcRoomRequestCommonParamBuilder: ...
    def build(self) -> MyAiVcRoomRequestCommonParam: ...
