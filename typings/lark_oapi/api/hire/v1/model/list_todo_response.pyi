from .list_todo_response_body import ListTodoResponseBody as ListTodoResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTodoResponse(BaseResponse):
    data: ListTodoResponseBody | None
    def __init__(self, d=None) -> None: ...
