from .comment_at_info import CommentAtInfo as CommentAtInfo
from .comment_reply import CommentReply as CommentReply
from lark_oapi.core.construct import init as init

class Comment:
    id: int | None
    content: str | None
    create_time: int | None
    update_time: int | None
    is_delete: int | None
    replies: list[CommentReply] | None
    at_info_list: list[CommentAtInfo] | None
    commentator: str | None
    extra: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CommentBuilder: ...

class CommentBuilder:
    def __init__(self) -> None: ...
    def id(self, id: int) -> CommentBuilder: ...
    def content(self, content: str) -> CommentBuilder: ...
    def create_time(self, create_time: int) -> CommentBuilder: ...
    def update_time(self, update_time: int) -> CommentBuilder: ...
    def is_delete(self, is_delete: int) -> CommentBuilder: ...
    def replies(self, replies: list[CommentReply]) -> CommentBuilder: ...
    def at_info_list(self, at_info_list: list[CommentAtInfo]) -> CommentBuilder: ...
    def commentator(self, commentator: str) -> CommentBuilder: ...
    def extra(self, extra: str) -> CommentBuilder: ...
    def build(self) -> Comment: ...
