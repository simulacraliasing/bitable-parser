from lark_oapi.core.construct import init as init

class PatchFileCommentResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PatchFileCommentResponseBodyBuilder: ...

class PatchFileCommentResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> PatchFileCommentResponseBody: ...
