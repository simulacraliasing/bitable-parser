from lark_oapi.core.construct import init as init

class GetJobTitleRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetJobTitleRequestBodyBuilder: ...

class GetJobTitleRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> GetJobTitleRequestBody: ...
