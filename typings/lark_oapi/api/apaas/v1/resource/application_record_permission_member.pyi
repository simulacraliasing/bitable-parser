from ..model.batch_create_authorization_application_record_permission_member_request import BatchCreateAuthorizationApplicationRecordPermissionMemberRequest as BatchCreateAuthorizationApplicationRecordPermissionMemberRequest
from ..model.batch_create_authorization_application_record_permission_member_response import BatchCreateAuthorizationApplicationRecordPermissionMemberResponse as BatchCreateAuthorizationApplicationRecordPermissionMemberResponse
from ..model.batch_remove_authorization_application_record_permission_member_request import BatchRemoveAuthorizationApplicationRecordPermissionMemberRequest as BatchRemoveAuthorizationApplicationRecordPermissionMemberRequest
from ..model.batch_remove_authorization_application_record_permission_member_response import BatchRemoveAuthorizationApplicationRecordPermissionMemberResponse as BatchRemoveAuthorizationApplicationRecordPermissionMemberResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ApplicationRecordPermissionMember:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def batch_create_authorization(self, request: BatchCreateAuthorizationApplicationRecordPermissionMemberRequest, option: RequestOption | None = None) -> BatchCreateAuthorizationApplicationRecordPermissionMemberResponse: ...
    async def abatch_create_authorization(self, request: BatchCreateAuthorizationApplicationRecordPermissionMemberRequest, option: RequestOption | None = None) -> BatchCreateAuthorizationApplicationRecordPermissionMemberResponse: ...
    def batch_remove_authorization(self, request: BatchRemoveAuthorizationApplicationRecordPermissionMemberRequest, option: RequestOption | None = None) -> BatchRemoveAuthorizationApplicationRecordPermissionMemberResponse: ...
    async def abatch_remove_authorization(self, request: BatchRemoveAuthorizationApplicationRecordPermissionMemberRequest, option: RequestOption | None = None) -> BatchRemoveAuthorizationApplicationRecordPermissionMemberResponse: ...
