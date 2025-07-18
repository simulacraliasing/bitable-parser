from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetOfferSchemaRequest(BaseRequest):
    offer_schema_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetOfferSchemaRequestBuilder: ...

class GetOfferSchemaRequestBuilder:
    def __init__(self) -> None: ...
    def offer_schema_id(self, offer_schema_id: str) -> GetOfferSchemaRequestBuilder: ...
    def build(self) -> GetOfferSchemaRequest: ...
