from lark_oapi.core.construct import init as init

class StartMeetingRecordingResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> StartMeetingRecordingResponseBodyBuilder: ...

class StartMeetingRecordingResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> StartMeetingRecordingResponseBody: ...
