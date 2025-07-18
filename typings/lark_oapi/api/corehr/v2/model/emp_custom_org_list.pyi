from .custom_org_list import CustomOrgList as CustomOrgList
from lark_oapi.core.construct import init as init

class EmpCustomOrgList:
    custom_org_list: list[CustomOrgList] | None
    effective_time: str | None
    start_reason: str | None
    job_data_custom_org_id: str | None
    version_id: str | None
    object_api_name: str | None
    user_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> EmpCustomOrgListBuilder: ...

class EmpCustomOrgListBuilder:
    def __init__(self) -> None: ...
    def custom_org_list(self, custom_org_list: list[CustomOrgList]) -> EmpCustomOrgListBuilder: ...
    def effective_time(self, effective_time: str) -> EmpCustomOrgListBuilder: ...
    def start_reason(self, start_reason: str) -> EmpCustomOrgListBuilder: ...
    def job_data_custom_org_id(self, job_data_custom_org_id: str) -> EmpCustomOrgListBuilder: ...
    def version_id(self, version_id: str) -> EmpCustomOrgListBuilder: ...
    def object_api_name(self, object_api_name: str) -> EmpCustomOrgListBuilder: ...
    def user_id(self, user_id: str) -> EmpCustomOrgListBuilder: ...
    def build(self) -> EmpCustomOrgList: ...
