from ..model.batch_get_employees_job_data_request import BatchGetEmployeesJobDataRequest as BatchGetEmployeesJobDataRequest
from ..model.batch_get_employees_job_data_response import BatchGetEmployeesJobDataResponse as BatchGetEmployeesJobDataResponse
from ..model.query_employees_job_data_request import QueryEmployeesJobDataRequest as QueryEmployeesJobDataRequest
from ..model.query_employees_job_data_response import QueryEmployeesJobDataResponse as QueryEmployeesJobDataResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class EmployeesJobData:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def batch_get(self, request: BatchGetEmployeesJobDataRequest, option: RequestOption | None = None) -> BatchGetEmployeesJobDataResponse: ...
    async def abatch_get(self, request: BatchGetEmployeesJobDataRequest, option: RequestOption | None = None) -> BatchGetEmployeesJobDataResponse: ...
    def query(self, request: QueryEmployeesJobDataRequest, option: RequestOption | None = None) -> QueryEmployeesJobDataResponse: ...
    async def aquery(self, request: QueryEmployeesJobDataRequest, option: RequestOption | None = None) -> QueryEmployeesJobDataResponse: ...
