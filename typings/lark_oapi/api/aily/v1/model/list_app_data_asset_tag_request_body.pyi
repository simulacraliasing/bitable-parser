from lark_oapi.core.construct import init as init

class ListAppDataAssetTagRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListAppDataAssetTagRequestBodyBuilder: ...

class ListAppDataAssetTagRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ListAppDataAssetTagRequestBody: ...
