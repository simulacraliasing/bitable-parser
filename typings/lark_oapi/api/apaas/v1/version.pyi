from .resource import *

class V1:
    application_audit_log: ApplicationAuditLog
    application_environment_variable: ApplicationEnvironmentVariable
    application_flow: ApplicationFlow
    application_function: ApplicationFunction
    application_object: ApplicationObject
    application_object_record: ApplicationObjectRecord
    application_record_permission_member: ApplicationRecordPermissionMember
    application_role_member: ApplicationRoleMember
    approval_instance: ApprovalInstance
    approval_task: ApprovalTask
    seat_activity: SeatActivity
    seat_assignment: SeatAssignment
    user_task: UserTask
    def __init__(self, config: Config) -> None: ...
