from lark_oapi.core.construct import init as init

class ListTaskCollaboratorRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListTaskCollaboratorRequestBodyBuilder: ...

class ListTaskCollaboratorRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ListTaskCollaboratorRequestBody: ...
