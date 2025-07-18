from ..model.create_tasklist_activity_subscription_request import CreateTasklistActivitySubscriptionRequest as CreateTasklistActivitySubscriptionRequest
from ..model.create_tasklist_activity_subscription_response import CreateTasklistActivitySubscriptionResponse as CreateTasklistActivitySubscriptionResponse
from ..model.delete_tasklist_activity_subscription_request import DeleteTasklistActivitySubscriptionRequest as DeleteTasklistActivitySubscriptionRequest
from ..model.delete_tasklist_activity_subscription_response import DeleteTasklistActivitySubscriptionResponse as DeleteTasklistActivitySubscriptionResponse
from ..model.get_tasklist_activity_subscription_request import GetTasklistActivitySubscriptionRequest as GetTasklistActivitySubscriptionRequest
from ..model.get_tasklist_activity_subscription_response import GetTasklistActivitySubscriptionResponse as GetTasklistActivitySubscriptionResponse
from ..model.list_tasklist_activity_subscription_request import ListTasklistActivitySubscriptionRequest as ListTasklistActivitySubscriptionRequest
from ..model.list_tasklist_activity_subscription_response import ListTasklistActivitySubscriptionResponse as ListTasklistActivitySubscriptionResponse
from ..model.patch_tasklist_activity_subscription_request import PatchTasklistActivitySubscriptionRequest as PatchTasklistActivitySubscriptionRequest
from ..model.patch_tasklist_activity_subscription_response import PatchTasklistActivitySubscriptionResponse as PatchTasklistActivitySubscriptionResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class TasklistActivitySubscription:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateTasklistActivitySubscriptionRequest, option: RequestOption | None = None) -> CreateTasklistActivitySubscriptionResponse: ...
    async def acreate(self, request: CreateTasklistActivitySubscriptionRequest, option: RequestOption | None = None) -> CreateTasklistActivitySubscriptionResponse: ...
    def delete(self, request: DeleteTasklistActivitySubscriptionRequest, option: RequestOption | None = None) -> DeleteTasklistActivitySubscriptionResponse: ...
    async def adelete(self, request: DeleteTasklistActivitySubscriptionRequest, option: RequestOption | None = None) -> DeleteTasklistActivitySubscriptionResponse: ...
    def get(self, request: GetTasklistActivitySubscriptionRequest, option: RequestOption | None = None) -> GetTasklistActivitySubscriptionResponse: ...
    async def aget(self, request: GetTasklistActivitySubscriptionRequest, option: RequestOption | None = None) -> GetTasklistActivitySubscriptionResponse: ...
    def list(self, request: ListTasklistActivitySubscriptionRequest, option: RequestOption | None = None) -> ListTasklistActivitySubscriptionResponse: ...
    async def alist(self, request: ListTasklistActivitySubscriptionRequest, option: RequestOption | None = None) -> ListTasklistActivitySubscriptionResponse: ...
    def patch(self, request: PatchTasklistActivitySubscriptionRequest, option: RequestOption | None = None) -> PatchTasklistActivitySubscriptionResponse: ...
    async def apatch(self, request: PatchTasklistActivitySubscriptionRequest, option: RequestOption | None = None) -> PatchTasklistActivitySubscriptionResponse: ...
