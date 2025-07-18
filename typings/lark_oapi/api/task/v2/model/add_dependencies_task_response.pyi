from .add_dependencies_task_response_body import AddDependenciesTaskResponseBody as AddDependenciesTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AddDependenciesTaskResponse(BaseResponse):
    data: AddDependenciesTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
