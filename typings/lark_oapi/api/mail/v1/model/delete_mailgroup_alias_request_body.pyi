from lark_oapi.core.construct import init as init

class DeleteMailgroupAliasRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteMailgroupAliasRequestBodyBuilder: ...

class DeleteMailgroupAliasRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteMailgroupAliasRequestBody: ...
