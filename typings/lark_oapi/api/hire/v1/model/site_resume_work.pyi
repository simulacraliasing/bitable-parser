from lark_oapi.core.construct import init as init

class SiteResumeWork:
    link: str | None
    description: str | None
    site_attachment_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SiteResumeWorkBuilder: ...

class SiteResumeWorkBuilder:
    def __init__(self) -> None: ...
    def link(self, link: str) -> SiteResumeWorkBuilder: ...
    def description(self, description: str) -> SiteResumeWorkBuilder: ...
    def site_attachment_id(self, site_attachment_id: str) -> SiteResumeWorkBuilder: ...
    def build(self) -> SiteResumeWork: ...
