from lark_oapi.core.construct import init as init

class ListAppWorkflowRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListAppWorkflowRequestBodyBuilder: ...

class ListAppWorkflowRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ListAppWorkflowRequestBody: ...
