from lark_oapi.core.construct import init as init

class ListWorkCityRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListWorkCityRequestBodyBuilder: ...

class ListWorkCityRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ListWorkCityRequestBody: ...
