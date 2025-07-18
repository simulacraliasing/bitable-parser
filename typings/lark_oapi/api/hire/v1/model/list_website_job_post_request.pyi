from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListWebsiteJobPostRequest(BaseRequest):
    page_token: str | None
    page_size: int | None
    user_id_type: str | None
    department_id_type: str | None
    job_level_id_type: str | None
    update_start_time: str | None
    update_end_time: str | None
    create_start_time: str | None
    create_end_time: str | None
    website_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListWebsiteJobPostRequestBuilder: ...

class ListWebsiteJobPostRequestBuilder:
    def __init__(self) -> None: ...
    def page_token(self, page_token: str) -> ListWebsiteJobPostRequestBuilder: ...
    def page_size(self, page_size: int) -> ListWebsiteJobPostRequestBuilder: ...
    def user_id_type(self, user_id_type: str) -> ListWebsiteJobPostRequestBuilder: ...
    def department_id_type(self, department_id_type: str) -> ListWebsiteJobPostRequestBuilder: ...
    def job_level_id_type(self, job_level_id_type: str) -> ListWebsiteJobPostRequestBuilder: ...
    def update_start_time(self, update_start_time: str) -> ListWebsiteJobPostRequestBuilder: ...
    def update_end_time(self, update_end_time: str) -> ListWebsiteJobPostRequestBuilder: ...
    def create_start_time(self, create_start_time: str) -> ListWebsiteJobPostRequestBuilder: ...
    def create_end_time(self, create_end_time: str) -> ListWebsiteJobPostRequestBuilder: ...
    def website_id(self, website_id: str) -> ListWebsiteJobPostRequestBuilder: ...
    def build(self) -> ListWebsiteJobPostRequest: ...
