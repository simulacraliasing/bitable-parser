from .get_process_form_variable_data_response_body import GetProcessFormVariableDataResponseBody as GetProcessFormVariableDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetProcessFormVariableDataResponse(BaseResponse):
    data: GetProcessFormVariableDataResponseBody | None
    def __init__(self, d=None) -> None: ...
