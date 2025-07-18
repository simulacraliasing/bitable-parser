from .get_resource_reservation_list_response_body import GetResourceReservationListResponseBody as GetResourceReservationListResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetResourceReservationListResponse(BaseResponse):
    data: GetResourceReservationListResponseBody | None
    def __init__(self, d=None) -> None: ...
