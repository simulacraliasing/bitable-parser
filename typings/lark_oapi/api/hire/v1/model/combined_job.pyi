from .combined_job_object_value_map import CombinedJobObjectValueMap as CombinedJobObjectValueMap
from .job_manager import JobManager as JobManager
from lark_oapi.core.construct import init as init

class CombinedJob:
    id: str | None
    code: str | None
    experience: int | None
    expiry_time: int | None
    customized_data_list: list[CombinedJobObjectValueMap] | None
    min_level_id: str | None
    min_salary: int | None
    title: str | None
    job_managers: JobManager | None
    job_process_id: str | None
    process_type: int | None
    subject_id: str | None
    job_function_id: str | None
    department_id: str | None
    head_count: int | None
    is_never_expired: bool | None
    max_salary: int | None
    requirement: str | None
    address_id: str | None
    description: str | None
    highlight_list: list[str] | None
    job_type_id: str | None
    max_level_id: str | None
    recruitment_type_id: str | None
    required_degree: int | None
    job_category_id: str | None
    address_id_list: list[str] | None
    job_attribute: int | None
    expiry_timestamp: str | None
    interview_registration_schema_id: str | None
    onboard_registration_schema_id: str | None
    target_major_id_list: list[str] | None
    portal_website_apply_form_schema_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CombinedJobBuilder: ...

class CombinedJobBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> CombinedJobBuilder: ...
    def code(self, code: str) -> CombinedJobBuilder: ...
    def experience(self, experience: int) -> CombinedJobBuilder: ...
    def expiry_time(self, expiry_time: int) -> CombinedJobBuilder: ...
    def customized_data_list(self, customized_data_list: list[CombinedJobObjectValueMap]) -> CombinedJobBuilder: ...
    def min_level_id(self, min_level_id: str) -> CombinedJobBuilder: ...
    def min_salary(self, min_salary: int) -> CombinedJobBuilder: ...
    def title(self, title: str) -> CombinedJobBuilder: ...
    def job_managers(self, job_managers: JobManager) -> CombinedJobBuilder: ...
    def job_process_id(self, job_process_id: str) -> CombinedJobBuilder: ...
    def process_type(self, process_type: int) -> CombinedJobBuilder: ...
    def subject_id(self, subject_id: str) -> CombinedJobBuilder: ...
    def job_function_id(self, job_function_id: str) -> CombinedJobBuilder: ...
    def department_id(self, department_id: str) -> CombinedJobBuilder: ...
    def head_count(self, head_count: int) -> CombinedJobBuilder: ...
    def is_never_expired(self, is_never_expired: bool) -> CombinedJobBuilder: ...
    def max_salary(self, max_salary: int) -> CombinedJobBuilder: ...
    def requirement(self, requirement: str) -> CombinedJobBuilder: ...
    def address_id(self, address_id: str) -> CombinedJobBuilder: ...
    def description(self, description: str) -> CombinedJobBuilder: ...
    def highlight_list(self, highlight_list: list[str]) -> CombinedJobBuilder: ...
    def job_type_id(self, job_type_id: str) -> CombinedJobBuilder: ...
    def max_level_id(self, max_level_id: str) -> CombinedJobBuilder: ...
    def recruitment_type_id(self, recruitment_type_id: str) -> CombinedJobBuilder: ...
    def required_degree(self, required_degree: int) -> CombinedJobBuilder: ...
    def job_category_id(self, job_category_id: str) -> CombinedJobBuilder: ...
    def address_id_list(self, address_id_list: list[str]) -> CombinedJobBuilder: ...
    def job_attribute(self, job_attribute: int) -> CombinedJobBuilder: ...
    def expiry_timestamp(self, expiry_timestamp: str) -> CombinedJobBuilder: ...
    def interview_registration_schema_id(self, interview_registration_schema_id: str) -> CombinedJobBuilder: ...
    def onboard_registration_schema_id(self, onboard_registration_schema_id: str) -> CombinedJobBuilder: ...
    def target_major_id_list(self, target_major_id_list: list[str]) -> CombinedJobBuilder: ...
    def portal_website_apply_form_schema_id(self, portal_website_apply_form_schema_id: str) -> CombinedJobBuilder: ...
    def build(self) -> CombinedJob: ...
