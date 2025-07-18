from .resource import *

class V1:
    alert: Alert
    export: Export
    meeting: Meeting
    meeting_recording: MeetingRecording
    meeting_list: MeetingList
    participant_list: ParticipantList
    participant_quality_list: ParticipantQualityList
    report: Report
    reserve: Reserve
    reserve_config: ReserveConfig
    reserve_config_admin: ReserveConfigAdmin
    reserve_config_disable_inform: ReserveConfigDisableInform
    reserve_config_form: ReserveConfigForm
    resource_reservation_list: ResourceReservationList
    room: Room
    room_config: RoomConfig
    room_level: RoomLevel
    scope_config: ScopeConfig
    def __init__(self, config: Config) -> None: ...
