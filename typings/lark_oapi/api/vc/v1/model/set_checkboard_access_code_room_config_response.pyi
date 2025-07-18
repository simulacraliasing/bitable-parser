from .set_checkboard_access_code_room_config_response_body import SetCheckboardAccessCodeRoomConfigResponseBody as SetCheckboardAccessCodeRoomConfigResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SetCheckboardAccessCodeRoomConfigResponse(BaseResponse):
    data: SetCheckboardAccessCodeRoomConfigResponseBody | None
    def __init__(self, d=None) -> None: ...
