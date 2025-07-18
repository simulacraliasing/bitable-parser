from ..model.add_sign_instance_request import AddSignInstanceRequest as AddSignInstanceRequest
from ..model.add_sign_instance_response import AddSignInstanceResponse as AddSignInstanceResponse
from ..model.cancel_instance_request import CancelInstanceRequest as CancelInstanceRequest
from ..model.cancel_instance_response import CancelInstanceResponse as CancelInstanceResponse
from ..model.cc_instance_request import CcInstanceRequest as CcInstanceRequest
from ..model.cc_instance_response import CcInstanceResponse as CcInstanceResponse
from ..model.create_instance_request import CreateInstanceRequest as CreateInstanceRequest
from ..model.create_instance_response import CreateInstanceResponse as CreateInstanceResponse
from ..model.get_instance_request import GetInstanceRequest as GetInstanceRequest
from ..model.get_instance_response import GetInstanceResponse as GetInstanceResponse
from ..model.list_instance_request import ListInstanceRequest as ListInstanceRequest
from ..model.list_instance_response import ListInstanceResponse as ListInstanceResponse
from ..model.preview_instance_request import PreviewInstanceRequest as PreviewInstanceRequest
from ..model.preview_instance_response import PreviewInstanceResponse as PreviewInstanceResponse
from ..model.query_instance_request import QueryInstanceRequest as QueryInstanceRequest
from ..model.query_instance_response import QueryInstanceResponse as QueryInstanceResponse
from ..model.search_cc_instance_request import SearchCcInstanceRequest as SearchCcInstanceRequest
from ..model.search_cc_instance_response import SearchCcInstanceResponse as SearchCcInstanceResponse
from ..model.specified_rollback_instance_request import SpecifiedRollbackInstanceRequest as SpecifiedRollbackInstanceRequest
from ..model.specified_rollback_instance_response import SpecifiedRollbackInstanceResponse as SpecifiedRollbackInstanceResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Instance:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def add_sign(self, request: AddSignInstanceRequest, option: RequestOption | None = None) -> AddSignInstanceResponse: ...
    async def aadd_sign(self, request: AddSignInstanceRequest, option: RequestOption | None = None) -> AddSignInstanceResponse: ...
    def cancel(self, request: CancelInstanceRequest, option: RequestOption | None = None) -> CancelInstanceResponse: ...
    async def acancel(self, request: CancelInstanceRequest, option: RequestOption | None = None) -> CancelInstanceResponse: ...
    def cc(self, request: CcInstanceRequest, option: RequestOption | None = None) -> CcInstanceResponse: ...
    async def acc(self, request: CcInstanceRequest, option: RequestOption | None = None) -> CcInstanceResponse: ...
    def create(self, request: CreateInstanceRequest, option: RequestOption | None = None) -> CreateInstanceResponse: ...
    async def acreate(self, request: CreateInstanceRequest, option: RequestOption | None = None) -> CreateInstanceResponse: ...
    def get(self, request: GetInstanceRequest, option: RequestOption | None = None) -> GetInstanceResponse: ...
    async def aget(self, request: GetInstanceRequest, option: RequestOption | None = None) -> GetInstanceResponse: ...
    def list(self, request: ListInstanceRequest, option: RequestOption | None = None) -> ListInstanceResponse: ...
    async def alist(self, request: ListInstanceRequest, option: RequestOption | None = None) -> ListInstanceResponse: ...
    def preview(self, request: PreviewInstanceRequest, option: RequestOption | None = None) -> PreviewInstanceResponse: ...
    async def apreview(self, request: PreviewInstanceRequest, option: RequestOption | None = None) -> PreviewInstanceResponse: ...
    def query(self, request: QueryInstanceRequest, option: RequestOption | None = None) -> QueryInstanceResponse: ...
    async def aquery(self, request: QueryInstanceRequest, option: RequestOption | None = None) -> QueryInstanceResponse: ...
    def search_cc(self, request: SearchCcInstanceRequest, option: RequestOption | None = None) -> SearchCcInstanceResponse: ...
    async def asearch_cc(self, request: SearchCcInstanceRequest, option: RequestOption | None = None) -> SearchCcInstanceResponse: ...
    def specified_rollback(self, request: SpecifiedRollbackInstanceRequest, option: RequestOption | None = None) -> SpecifiedRollbackInstanceResponse: ...
    async def aspecified_rollback(self, request: SpecifiedRollbackInstanceRequest, option: RequestOption | None = None) -> SpecifiedRollbackInstanceResponse: ...
