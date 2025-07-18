from .combined_job_result_default_job_post import CombinedJobResultDefaultJobPost as CombinedJobResultDefaultJobPost
from .job import Job as Job
from .job_manager import JobManager as JobManager
from .registration_schema_info import RegistrationSchemaInfo as RegistrationSchemaInfo
from .target_major_info import TargetMajorInfo as TargetMajorInfo
from lark_oapi.core.construct import init as init

class CombinedCreateJobResponseBody:
    default_job_post: CombinedJobResultDefaultJobPost | None
    job: Job | None
    job_manager: JobManager | None
    interview_registration_schema_info: RegistrationSchemaInfo | None
    onboard_registration_schema_info: RegistrationSchemaInfo | None
    target_major_list: list[TargetMajorInfo] | None
    portal_website_apply_form_schema_info: RegistrationSchemaInfo | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CombinedCreateJobResponseBodyBuilder: ...

class CombinedCreateJobResponseBodyBuilder:
    def __init__(self) -> None: ...
    def default_job_post(self, default_job_post: CombinedJobResultDefaultJobPost) -> CombinedCreateJobResponseBodyBuilder: ...
    def job(self, job: Job) -> CombinedCreateJobResponseBodyBuilder: ...
    def job_manager(self, job_manager: JobManager) -> CombinedCreateJobResponseBodyBuilder: ...
    def interview_registration_schema_info(self, interview_registration_schema_info: RegistrationSchemaInfo) -> CombinedCreateJobResponseBodyBuilder: ...
    def onboard_registration_schema_info(self, onboard_registration_schema_info: RegistrationSchemaInfo) -> CombinedCreateJobResponseBodyBuilder: ...
    def target_major_list(self, target_major_list: list[TargetMajorInfo]) -> CombinedCreateJobResponseBodyBuilder: ...
    def portal_website_apply_form_schema_info(self, portal_website_apply_form_schema_info: RegistrationSchemaInfo) -> CombinedCreateJobResponseBodyBuilder: ...
    def build(self) -> CombinedCreateJobResponseBody: ...
