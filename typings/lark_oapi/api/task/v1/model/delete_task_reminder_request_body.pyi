from lark_oapi.core.construct import init as init

class DeleteTaskReminderRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteTaskReminderRequestBodyBuilder: ...

class DeleteTaskReminderRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteTaskReminderRequestBody: ...
