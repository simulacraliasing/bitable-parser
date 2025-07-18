from .find_by_department_user_response_body import FindByDepartmentUserResponseBody as FindByDepartmentUserResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class FindByDepartmentUserResponse(BaseResponse):
    data: FindByDepartmentUserResponseBody | None
    def __init__(self, d=None) -> None: ...
