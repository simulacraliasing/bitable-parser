from lark_oapi.core.construct import init as init

class GetMeetingRecordingRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetMeetingRecordingRequestBodyBuilder: ...

class GetMeetingRecordingRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> GetMeetingRecordingRequestBody: ...
