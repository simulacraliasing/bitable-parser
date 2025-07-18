from .offer_schema_detail import OfferSchemaDetail as OfferSchemaDetail
from lark_oapi.core.construct import init as init

class GetOfferSchemaResponseBody:
    id: str | None
    scenario: int | None
    version: int | None
    object_list: list[OfferSchemaDetail] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetOfferSchemaResponseBodyBuilder: ...

class GetOfferSchemaResponseBodyBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> GetOfferSchemaResponseBodyBuilder: ...
    def scenario(self, scenario: int) -> GetOfferSchemaResponseBodyBuilder: ...
    def version(self, version: int) -> GetOfferSchemaResponseBodyBuilder: ...
    def object_list(self, object_list: list[OfferSchemaDetail]) -> GetOfferSchemaResponseBodyBuilder: ...
    def build(self) -> GetOfferSchemaResponseBody: ...
