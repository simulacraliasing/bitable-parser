from lark_oapi.core.construct import init as init

class ExecuteApplicationFlowResponseBody:
    status: str | None
    out_params: str | None
    execution_id: str | None
    error_msg: str | None
    code: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ExecuteApplicationFlowResponseBodyBuilder: ...

class ExecuteApplicationFlowResponseBodyBuilder:
    def __init__(self) -> None: ...
    def status(self, status: str) -> ExecuteApplicationFlowResponseBodyBuilder: ...
    def out_params(self, out_params: str) -> ExecuteApplicationFlowResponseBodyBuilder: ...
    def execution_id(self, execution_id: str) -> ExecuteApplicationFlowResponseBodyBuilder: ...
    def error_msg(self, error_msg: str) -> ExecuteApplicationFlowResponseBodyBuilder: ...
    def code(self, code: str) -> ExecuteApplicationFlowResponseBodyBuilder: ...
    def build(self) -> ExecuteApplicationFlowResponseBody: ...
