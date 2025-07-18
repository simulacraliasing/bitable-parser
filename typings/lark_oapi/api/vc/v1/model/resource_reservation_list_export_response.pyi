from .resource_reservation_list_export_response_body import ResourceReservationListExportResponseBody as ResourceReservationListExportResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ResourceReservationListExportResponse(BaseResponse):
    data: ResourceReservationListExportResponseBody | None
    def __init__(self, d=None) -> None: ...
