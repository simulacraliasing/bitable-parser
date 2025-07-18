from ..model.create_job_requirement_request import CreateJobRequirementRequest as CreateJobRequirementRequest
from ..model.create_job_requirement_response import CreateJobRequirementResponse as CreateJobRequirementResponse
from ..model.delete_job_requirement_request import DeleteJobRequirementRequest as DeleteJobRequirementRequest
from ..model.delete_job_requirement_response import DeleteJobRequirementResponse as DeleteJobRequirementResponse
from ..model.list_by_id_job_requirement_request import ListByIdJobRequirementRequest as ListByIdJobRequirementRequest
from ..model.list_by_id_job_requirement_response import ListByIdJobRequirementResponse as ListByIdJobRequirementResponse
from ..model.list_job_requirement_request import ListJobRequirementRequest as ListJobRequirementRequest
from ..model.list_job_requirement_response import ListJobRequirementResponse as ListJobRequirementResponse
from ..model.update_job_requirement_request import UpdateJobRequirementRequest as UpdateJobRequirementRequest
from ..model.update_job_requirement_response import UpdateJobRequirementResponse as UpdateJobRequirementResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class JobRequirement:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateJobRequirementRequest, option: RequestOption | None = None) -> CreateJobRequirementResponse: ...
    async def acreate(self, request: CreateJobRequirementRequest, option: RequestOption | None = None) -> CreateJobRequirementResponse: ...
    def delete(self, request: DeleteJobRequirementRequest, option: RequestOption | None = None) -> DeleteJobRequirementResponse: ...
    async def adelete(self, request: DeleteJobRequirementRequest, option: RequestOption | None = None) -> DeleteJobRequirementResponse: ...
    def list(self, request: ListJobRequirementRequest, option: RequestOption | None = None) -> ListJobRequirementResponse: ...
    async def alist(self, request: ListJobRequirementRequest, option: RequestOption | None = None) -> ListJobRequirementResponse: ...
    def list_by_id(self, request: ListByIdJobRequirementRequest, option: RequestOption | None = None) -> ListByIdJobRequirementResponse: ...
    async def alist_by_id(self, request: ListByIdJobRequirementRequest, option: RequestOption | None = None) -> ListByIdJobRequirementResponse: ...
    def update(self, request: UpdateJobRequirementRequest, option: RequestOption | None = None) -> UpdateJobRequirementResponse: ...
    async def aupdate(self, request: UpdateJobRequirementRequest, option: RequestOption | None = None) -> UpdateJobRequirementResponse: ...
