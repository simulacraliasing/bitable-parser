from lark_oapi.core.construct import init as init

class ApprovalComment:
    id: str | None
    commenter: str | None
    content: str | None
    create_at: str | None
    update_at: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ApprovalCommentBuilder: ...

class ApprovalCommentBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> ApprovalCommentBuilder: ...
    def commenter(self, commenter: str) -> ApprovalCommentBuilder: ...
    def content(self, content: str) -> ApprovalCommentBuilder: ...
    def create_at(self, create_at: str) -> ApprovalCommentBuilder: ...
    def update_at(self, update_at: str) -> ApprovalCommentBuilder: ...
    def build(self) -> ApprovalComment: ...
