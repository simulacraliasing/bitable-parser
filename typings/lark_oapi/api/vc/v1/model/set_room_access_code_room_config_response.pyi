from .set_room_access_code_room_config_response_body import SetRoomAccessCodeRoomConfigResponseBody as SetRoomAccessCodeRoomConfigResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SetRoomAccessCodeRoomConfigResponse(BaseResponse):
    data: SetRoomAccessCodeRoomConfigResponseBody | None
    def __init__(self, d=None) -> None: ...
