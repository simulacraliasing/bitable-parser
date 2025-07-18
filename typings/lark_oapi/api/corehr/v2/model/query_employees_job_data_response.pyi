from .query_employees_job_data_response_body import QueryEmployeesJobDataResponseBody as QueryEmployeesJobDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryEmployeesJobDataResponse(BaseResponse):
    data: QueryEmployeesJobDataResponseBody | None
    def __init__(self, d=None) -> None: ...
