from lark_oapi.core.construct import init as init

class BatchQueryExternalBackgroundCheckRequestBody:
    external_background_check_id_list: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BatchQueryExternalBackgroundCheckRequestBodyBuilder: ...

class BatchQueryExternalBackgroundCheckRequestBodyBuilder:
    def __init__(self) -> None: ...
    def external_background_check_id_list(self, external_background_check_id_list: list[str]) -> BatchQueryExternalBackgroundCheckRequestBodyBuilder: ...
    def build(self) -> BatchQueryExternalBackgroundCheckRequestBody: ...
