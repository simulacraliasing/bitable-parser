from lark_oapi.core.construct import init as init

class PreviewNotificationResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PreviewNotificationResponseBodyBuilder: ...

class PreviewNotificationResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> PreviewNotificationResponseBody: ...
