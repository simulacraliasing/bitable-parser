from lark_oapi.core.construct import init as init

class DeleteExchangeBindingRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteExchangeBindingRequestBodyBuilder: ...

class DeleteExchangeBindingRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteExchangeBindingRequestBody: ...
