from .resource import *

class V1:
    approval_info: ApprovalInfo
    archive_rule: ArchiveRule
    file: File
    group: Group
    leave_accrual_record: LeaveAccrualRecord
    leave_employ_expire_record: LeaveEmployExpireRecord
    shift: Shift
    user_approval: UserApproval
    user_daily_shift: UserDailyShift
    user_flow: UserFlow
    user_setting: UserSetting
    user_stats_data: UserStatsData
    user_stats_field: UserStatsField
    user_stats_view: UserStatsView
    user_task: UserTask
    user_task_remedy: UserTaskRemedy
    def __init__(self, config: Config) -> None: ...
