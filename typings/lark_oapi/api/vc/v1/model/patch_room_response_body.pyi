from lark_oapi.core.construct import init as init

class PatchRoomResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PatchRoomResponseBodyBuilder: ...

class PatchRoomResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> PatchRoomResponseBody: ...
