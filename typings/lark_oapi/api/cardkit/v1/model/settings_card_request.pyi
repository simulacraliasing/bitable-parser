from .settings_card_request_body import SettingsCardRequestBody as SettingsCardRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class SettingsCardRequest(BaseRequest):
    card_id: str | None
    request_body: SettingsCardRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> SettingsCardRequestBuilder: ...

class SettingsCardRequestBuilder:
    def __init__(self) -> None: ...
    def card_id(self, card_id: str) -> SettingsCardRequestBuilder: ...
    def request_body(self, request_body: SettingsCardRequestBody) -> SettingsCardRequestBuilder: ...
    def build(self) -> SettingsCardRequest: ...
