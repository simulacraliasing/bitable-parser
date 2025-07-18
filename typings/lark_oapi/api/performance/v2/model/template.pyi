from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class Template:
    template_id: str | None
    name: I18n | None
    stage_type: str | None
    review_stage_role: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TemplateBuilder: ...

class TemplateBuilder:
    def __init__(self) -> None: ...
    def template_id(self, template_id: str) -> TemplateBuilder: ...
    def name(self, name: I18n) -> TemplateBuilder: ...
    def stage_type(self, stage_type: str) -> TemplateBuilder: ...
    def review_stage_role(self, review_stage_role: str) -> TemplateBuilder: ...
    def build(self) -> Template: ...
