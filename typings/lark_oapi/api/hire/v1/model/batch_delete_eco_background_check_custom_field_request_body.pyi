from lark_oapi.core.construct import init as init

class BatchDeleteEcoBackgroundCheckCustomFieldRequestBody:
    account_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BatchDeleteEcoBackgroundCheckCustomFieldRequestBodyBuilder: ...

class BatchDeleteEcoBackgroundCheckCustomFieldRequestBodyBuilder:
    def __init__(self) -> None: ...
    def account_id(self, account_id: str) -> BatchDeleteEcoBackgroundCheckCustomFieldRequestBodyBuilder: ...
    def build(self) -> BatchDeleteEcoBackgroundCheckCustomFieldRequestBody: ...
