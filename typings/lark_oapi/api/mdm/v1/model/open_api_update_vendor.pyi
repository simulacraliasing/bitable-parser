from lark_oapi.core.construct import init as init

class OpenApiUpdateVendor:
    id: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> OpenApiUpdateVendorBuilder: ...

class OpenApiUpdateVendorBuilder:
    def __init__(self) -> None: ...
    def id(self, id: int) -> OpenApiUpdateVendorBuilder: ...
    def build(self) -> OpenApiUpdateVendor: ...
