from ..model.get_user_face_request import GetUserFaceRequest as GetUserFaceRequest
from ..model.get_user_face_response import GetUserFaceResponse as GetUserFaceResponse
from ..model.update_user_face_request import UpdateUserFaceRequest as UpdateUserFaceRequest
from ..model.update_user_face_response import UpdateUserFaceResponse as UpdateUserFaceResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class UserFace:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetUserFaceRequest, option: RequestOption | None = None) -> GetUserFaceResponse: ...
    async def aget(self, request: GetUserFaceRequest, option: RequestOption | None = None) -> GetUserFaceResponse: ...
    def update(self, request: UpdateUserFaceRequest, option: RequestOption | None = None) -> UpdateUserFaceResponse: ...
    async def aupdate(self, request: UpdateUserFaceRequest, option: RequestOption | None = None) -> UpdateUserFaceResponse: ...
