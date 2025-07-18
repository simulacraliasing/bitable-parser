from .update_result_eco_background_check_request_body import UpdateResultEcoBackgroundCheckRequestBody as UpdateResultEcoBackgroundCheckRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class UpdateResultEcoBackgroundCheckRequest(BaseRequest):
    request_body: UpdateResultEcoBackgroundCheckRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> UpdateResultEcoBackgroundCheckRequestBuilder: ...

class UpdateResultEcoBackgroundCheckRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: UpdateResultEcoBackgroundCheckRequestBody) -> UpdateResultEcoBackgroundCheckRequestBuilder: ...
    def build(self) -> UpdateResultEcoBackgroundCheckRequest: ...
