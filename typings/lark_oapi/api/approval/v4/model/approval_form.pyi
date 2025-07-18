from lark_oapi.core.construct import init as init

class ApprovalForm:
    form_content: str | None
    widget_relation: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ApprovalFormBuilder: ...

class ApprovalFormBuilder:
    def __init__(self) -> None: ...
    def form_content(self, form_content: str) -> ApprovalFormBuilder: ...
    def widget_relation(self, widget_relation: str) -> ApprovalFormBuilder: ...
    def build(self) -> ApprovalForm: ...
