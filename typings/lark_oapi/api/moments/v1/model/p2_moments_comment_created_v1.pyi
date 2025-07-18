from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2MomentsCommentCreatedV1Data:
    user_id: UserId | None
    id: str | None
    create_time: str | None
    post_id: str | None
    reply_comment_id: str | None
    root_comment_id: str | None
    user_type: int | None
    def __init__(self, d=None) -> None: ...

class P2MomentsCommentCreatedV1(EventContext):
    event: P2MomentsCommentCreatedV1Data | None
    def __init__(self, d=None) -> None: ...
