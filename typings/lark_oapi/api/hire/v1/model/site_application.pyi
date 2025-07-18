from .site_application_resume import SiteApplicationResume as SiteApplicationResume
from lark_oapi.core.construct import init as init

class SiteApplication:
    external_id: str | None
    job_post_id: str | None
    resume: SiteApplicationResume | None
    status: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SiteApplicationBuilder: ...

class SiteApplicationBuilder:
    def __init__(self) -> None: ...
    def external_id(self, external_id: str) -> SiteApplicationBuilder: ...
    def job_post_id(self, job_post_id: str) -> SiteApplicationBuilder: ...
    def resume(self, resume: SiteApplicationResume) -> SiteApplicationBuilder: ...
    def status(self, status: str) -> SiteApplicationBuilder: ...
    def build(self) -> SiteApplication: ...
