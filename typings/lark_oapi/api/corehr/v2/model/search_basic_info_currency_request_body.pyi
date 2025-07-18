from lark_oapi.core.construct import init as init

class SearchBasicInfoCurrencyRequestBody:
    currency_id_list: list[str] | None
    status_list: list[int] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SearchBasicInfoCurrencyRequestBodyBuilder: ...

class SearchBasicInfoCurrencyRequestBodyBuilder:
    def __init__(self) -> None: ...
    def currency_id_list(self, currency_id_list: list[str]) -> SearchBasicInfoCurrencyRequestBodyBuilder: ...
    def status_list(self, status_list: list[int]) -> SearchBasicInfoCurrencyRequestBodyBuilder: ...
    def build(self) -> SearchBasicInfoCurrencyRequestBody: ...
