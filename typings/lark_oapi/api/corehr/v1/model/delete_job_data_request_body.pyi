from lark_oapi.core.construct import init as init

class DeleteJobDataRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteJobDataRequestBodyBuilder: ...

class DeleteJobDataRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteJobDataRequestBody: ...
