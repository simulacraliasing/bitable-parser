from .meeting_event_meeting import MeetingEventMeeting as MeetingEventMeeting
from .meeting_event_user import MeetingEventUser as MeetingEventUser
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2VcMeetingRecordingEndedV1Data:
    meeting: MeetingEventMeeting | None
    operator: MeetingEventUser | None
    def __init__(self, d=None) -> None: ...

class P2VcMeetingRecordingEndedV1(EventContext):
    event: P2VcMeetingRecordingEndedV1Data | None
    def __init__(self, d=None) -> None: ...
