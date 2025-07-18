from lark_oapi.core.construct import init as init

class WebsiteDeliveryDto:
    application_id: str | None
    id: str | None
    job_id: str | None
    job_post_id: str | None
    portal_resume_id: str | None
    user_id: str | None
    talent_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> WebsiteDeliveryDtoBuilder: ...

class WebsiteDeliveryDtoBuilder:
    def __init__(self) -> None: ...
    def application_id(self, application_id: str) -> WebsiteDeliveryDtoBuilder: ...
    def id(self, id: str) -> WebsiteDeliveryDtoBuilder: ...
    def job_id(self, job_id: str) -> WebsiteDeliveryDtoBuilder: ...
    def job_post_id(self, job_post_id: str) -> WebsiteDeliveryDtoBuilder: ...
    def portal_resume_id(self, portal_resume_id: str) -> WebsiteDeliveryDtoBuilder: ...
    def user_id(self, user_id: str) -> WebsiteDeliveryDtoBuilder: ...
    def talent_id(self, talent_id: str) -> WebsiteDeliveryDtoBuilder: ...
    def build(self) -> WebsiteDeliveryDto: ...
