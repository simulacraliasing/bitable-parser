from .get_by_param_custom_field_response_body import GetByParamCustomFieldResponseBody as GetByParamCustomFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetByParamCustomFieldResponse(BaseResponse):
    data: GetByParamCustomFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
