from lark_oapi.core.construct import init as init

class DeleteCommentResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteCommentResponseBodyBuilder: ...

class DeleteCommentResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteCommentResponseBody: ...
