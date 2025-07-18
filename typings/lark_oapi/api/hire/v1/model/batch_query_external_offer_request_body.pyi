from lark_oapi.core.construct import init as init

class BatchQueryExternalOfferRequestBody:
    external_offer_id_list: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BatchQueryExternalOfferRequestBodyBuilder: ...

class BatchQueryExternalOfferRequestBodyBuilder:
    def __init__(self) -> None: ...
    def external_offer_id_list(self, external_offer_id_list: list[str]) -> BatchQueryExternalOfferRequestBodyBuilder: ...
    def build(self) -> BatchQueryExternalOfferRequestBody: ...
