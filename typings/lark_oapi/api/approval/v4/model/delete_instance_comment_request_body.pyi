from lark_oapi.core.construct import init as init

class DeleteInstanceCommentRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteInstanceCommentRequestBodyBuilder: ...

class DeleteInstanceCommentRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteInstanceCommentRequestBody: ...
