from .resource import *

class V3:
    custom_attr: CustomAttr
    custom_attr_event: CustomAttrEvent
    department: Department
    employee_type_enum: EmployeeTypeEnum
    functional_role: FunctionalRole
    functional_role_member: FunctionalRoleMember
    group: Group
    group_member: GroupMember
    job_family: JobFamily
    job_level: JobLevel
    job_title: JobTitle
    scope: Scope
    unit: Unit
    user: User
    work_city: WorkCity
    def __init__(self, config: Config) -> None: ...
