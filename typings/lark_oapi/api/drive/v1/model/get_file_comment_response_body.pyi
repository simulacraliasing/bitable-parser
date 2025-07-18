from .reply_list import ReplyList as ReplyList
from lark_oapi.core.construct import init as init

class GetFileCommentResponseBody:
    comment_id: str | None
    user_id: str | None
    create_time: int | None
    update_time: int | None
    is_solved: bool | None
    solved_time: int | None
    solver_user_id: str | None
    has_more: bool | None
    page_token: str | None
    is_whole: bool | None
    quote: str | None
    reply_list: ReplyList | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetFileCommentResponseBodyBuilder: ...

class GetFileCommentResponseBodyBuilder:
    def __init__(self) -> None: ...
    def comment_id(self, comment_id: str) -> GetFileCommentResponseBodyBuilder: ...
    def user_id(self, user_id: str) -> GetFileCommentResponseBodyBuilder: ...
    def create_time(self, create_time: int) -> GetFileCommentResponseBodyBuilder: ...
    def update_time(self, update_time: int) -> GetFileCommentResponseBodyBuilder: ...
    def is_solved(self, is_solved: bool) -> GetFileCommentResponseBodyBuilder: ...
    def solved_time(self, solved_time: int) -> GetFileCommentResponseBodyBuilder: ...
    def solver_user_id(self, solver_user_id: str) -> GetFileCommentResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> GetFileCommentResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> GetFileCommentResponseBodyBuilder: ...
    def is_whole(self, is_whole: bool) -> GetFileCommentResponseBodyBuilder: ...
    def quote(self, quote: str) -> GetFileCommentResponseBodyBuilder: ...
    def reply_list(self, reply_list: ReplyList) -> GetFileCommentResponseBodyBuilder: ...
    def build(self) -> GetFileCommentResponseBody: ...
