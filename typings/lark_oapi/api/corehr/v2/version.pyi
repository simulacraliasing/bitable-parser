from .resource import *

class V2:
    approval_groups: ApprovalGroups
    approver: Approver
    basic_info_bank: BasicInfoBank
    basic_info_bank_branch: BasicInfoBankBranch
    basic_info_city: BasicInfoCity
    basic_info_country_region: BasicInfoCountryRegion
    basic_info_country_region_subdivision: BasicInfoCountryRegionSubdivision
    basic_info_currency: BasicInfoCurrency
    basic_info_district: BasicInfoDistrict
    basic_info_language: BasicInfoLanguage
    basic_info_nationality: BasicInfoNationality
    basic_info_time_zone: BasicInfoTimeZone
    bp: Bp
    company: Company
    contract: Contract
    cost_allocation: CostAllocation
    cost_center: CostCenter
    cost_center_version: CostCenterVersion
    custom_org: CustomOrg
    default_cost_center: DefaultCostCenter
    department: Department
    employee: Employee
    employees_additional_job: EmployeesAdditionalJob
    employees_bp: EmployeesBp
    employees_international_assignment: EmployeesInternationalAssignment
    employees_job_data: EmployeesJobData
    enum: Enum
    job: Job
    job_change: JobChange
    job_family: JobFamily
    job_grade: JobGrade
    job_level: JobLevel
    location: Location
    location_address: LocationAddress
    offboarding: Offboarding
    person: Person
    pre_hire: PreHire
    probation: Probation
    probation_assessment: ProbationAssessment
    process: Process
    process_approver: ProcessApprover
    process_cc: ProcessCc
    process_extra: ProcessExtra
    process_form_variable_data: ProcessFormVariableData
    process_node: ProcessNode
    process_status: ProcessStatus
    process_transfer: ProcessTransfer
    process_revoke: ProcessRevoke
    process_withdraw: ProcessWithdraw
    report_detail_row: ReportDetailRow
    workforce_plan: WorkforcePlan
    workforce_plan_detail: WorkforcePlanDetail
    workforce_plan_detail_row: WorkforcePlanDetailRow
    def __init__(self, config: Config) -> None: ...
