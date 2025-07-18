from ..model.create_user_mailbox_mail_contact_request import CreateUserMailboxMailContactRequest as CreateUserMailboxMailContactRequest
from ..model.create_user_mailbox_mail_contact_response import CreateUserMailboxMailContactResponse as CreateUserMailboxMailContactResponse
from ..model.delete_user_mailbox_mail_contact_request import DeleteUserMailboxMailContactRequest as DeleteUserMailboxMailContactRequest
from ..model.delete_user_mailbox_mail_contact_response import DeleteUserMailboxMailContactResponse as DeleteUserMailboxMailContactResponse
from ..model.list_user_mailbox_mail_contact_request import ListUserMailboxMailContactRequest as ListUserMailboxMailContactRequest
from ..model.list_user_mailbox_mail_contact_response import ListUserMailboxMailContactResponse as ListUserMailboxMailContactResponse
from ..model.patch_user_mailbox_mail_contact_request import PatchUserMailboxMailContactRequest as PatchUserMailboxMailContactRequest
from ..model.patch_user_mailbox_mail_contact_response import PatchUserMailboxMailContactResponse as PatchUserMailboxMailContactResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class UserMailboxMailContact:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateUserMailboxMailContactRequest, option: RequestOption | None = None) -> CreateUserMailboxMailContactResponse: ...
    async def acreate(self, request: CreateUserMailboxMailContactRequest, option: RequestOption | None = None) -> CreateUserMailboxMailContactResponse: ...
    def delete(self, request: DeleteUserMailboxMailContactRequest, option: RequestOption | None = None) -> DeleteUserMailboxMailContactResponse: ...
    async def adelete(self, request: DeleteUserMailboxMailContactRequest, option: RequestOption | None = None) -> DeleteUserMailboxMailContactResponse: ...
    def list(self, request: ListUserMailboxMailContactRequest, option: RequestOption | None = None) -> ListUserMailboxMailContactResponse: ...
    async def alist(self, request: ListUserMailboxMailContactRequest, option: RequestOption | None = None) -> ListUserMailboxMailContactResponse: ...
    def patch(self, request: PatchUserMailboxMailContactRequest, option: RequestOption | None = None) -> PatchUserMailboxMailContactResponse: ...
    async def apatch(self, request: PatchUserMailboxMailContactRequest, option: RequestOption | None = None) -> PatchUserMailboxMailContactResponse: ...
