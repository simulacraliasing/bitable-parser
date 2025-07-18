from lark_oapi.core.construct import init as init

class TaskTransfer:
    approval_code: str | None
    instance_code: str | None
    user_id: str | None
    comment: str | None
    transfer_user_id: str | None
    task_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TaskTransferBuilder: ...

class TaskTransferBuilder:
    def __init__(self) -> None: ...
    def approval_code(self, approval_code: str) -> TaskTransferBuilder: ...
    def instance_code(self, instance_code: str) -> TaskTransferBuilder: ...
    def user_id(self, user_id: str) -> TaskTransferBuilder: ...
    def comment(self, comment: str) -> TaskTransferBuilder: ...
    def transfer_user_id(self, transfer_user_id: str) -> TaskTransferBuilder: ...
    def task_id(self, task_id: str) -> TaskTransferBuilder: ...
    def build(self) -> TaskTransfer: ...
