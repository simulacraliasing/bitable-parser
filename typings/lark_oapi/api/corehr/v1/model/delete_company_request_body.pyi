from lark_oapi.core.construct import init as init

class DeleteCompanyRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteCompanyRequestBodyBuilder: ...

class DeleteCompanyRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteCompanyRequestBody: ...
