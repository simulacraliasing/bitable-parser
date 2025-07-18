from .meeting_event_meeting import MeetingEventMeeting as MeetingEventMeeting
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2VcMeetingRecordingReadyV1Data:
    meeting: MeetingEventMeeting | None
    url: str | None
    duration: int | None
    def __init__(self, d=None) -> None: ...

class P2VcMeetingRecordingReadyV1(EventContext):
    event: P2VcMeetingRecordingReadyV1Data | None
    def __init__(self, d=None) -> None: ...
