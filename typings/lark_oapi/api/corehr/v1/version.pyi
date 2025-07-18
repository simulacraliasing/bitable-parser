from .resource import *

class V1:
    assigned_user: AssignedUser
    authorization: Authorization
    common_data_id: CommonDataId
    common_data_meta_data: CommonDataMetaData
    company: Company
    compensation_standard: CompensationStandard
    contract: Contract
    country_region: CountryRegion
    currency: Currency
    custom_field: CustomField
    department: Department
    employee_type: EmployeeType
    employment: Employment
    file: File
    job: Job
    job_change: JobChange
    job_data: JobData
    job_family: JobFamily
    job_level: JobLevel
    leave: Leave
    leave_granting_record: LeaveGrantingRecord
    location: Location
    national_id_type: NationalIdType
    offboarding: Offboarding
    org_role_authorization: OrgRoleAuthorization
    person: Person
    pre_hire: PreHire
    process_form_variable_data: ProcessFormVariableData
    security_group: SecurityGroup
    subdivision: Subdivision
    subregion: Subregion
    transfer_reason: TransferReason
    transfer_type: TransferType
    working_hours_type: WorkingHoursType
    def __init__(self, config: Config) -> None: ...
