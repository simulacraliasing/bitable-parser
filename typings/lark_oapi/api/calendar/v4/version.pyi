from .resource import *

class V4:
    calendar: Calendar
    calendar_acl: CalendarAcl
    calendar_event: CalendarEvent
    calendar_event_attendee: CalendarEventAttendee
    calendar_event_attendee_chat_member: CalendarEventAttendeeChatMember
    calendar_event_meeting_chat: CalendarEventMeetingChat
    calendar_event_meeting_minute: CalendarEventMeetingMinute
    exchange_binding: ExchangeBinding
    freebusy: Freebusy
    setting: Setting
    timeoff_event: TimeoffEvent
    def __init__(self, config: Config) -> None: ...
