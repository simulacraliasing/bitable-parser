from lark_oapi.core.construct import init as init

class SetRoomConfigResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SetRoomConfigResponseBodyBuilder: ...

class SetRoomConfigResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> SetRoomConfigResponseBody: ...
