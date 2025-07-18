from .room_digital_signage import RoomDigitalSignage as RoomDigitalSignage
from .room_status import RoomStatus as RoomStatus
from lark_oapi.core.construct import init as init

class RoomConfig:
    room_background: str | None
    display_background: str | None
    digital_signage: RoomDigitalSignage | None
    room_box_digital_signage: RoomDigitalSignage | None
    room_status: RoomStatus | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RoomConfigBuilder: ...

class RoomConfigBuilder:
    def __init__(self) -> None: ...
    def room_background(self, room_background: str) -> RoomConfigBuilder: ...
    def display_background(self, display_background: str) -> RoomConfigBuilder: ...
    def digital_signage(self, digital_signage: RoomDigitalSignage) -> RoomConfigBuilder: ...
    def room_box_digital_signage(self, room_box_digital_signage: RoomDigitalSignage) -> RoomConfigBuilder: ...
    def room_status(self, room_status: RoomStatus) -> RoomConfigBuilder: ...
    def build(self) -> RoomConfig: ...
