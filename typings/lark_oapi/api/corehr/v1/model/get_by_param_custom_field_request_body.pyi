from lark_oapi.core.construct import init as init

class GetByParamCustomFieldRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetByParamCustomFieldRequestBodyBuilder: ...

class GetByParamCustomFieldRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> GetByParamCustomFieldRequestBody: ...
