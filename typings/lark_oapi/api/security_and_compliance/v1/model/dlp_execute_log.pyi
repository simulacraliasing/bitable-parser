from .dlp_evidence_detail import DlpEvidenceDetail as DlpEvidenceDetail
from .dlp_hit_policy import DlpHitPolicy as DlpHitPolicy
from lark_oapi.core.construct import init as init

class DlpExecuteLog:
    applicable_service: str | None
    user_name: str | None
    user_id: int | None
    trigger: str | None
    time: int | None
    system_action: str | None
    sender_name: str | None
    sender_id: int | None
    recipient_name: str | None
    recipient_id: int | None
    chat_name: str | None
    chat_id: int | None
    message_id: int | None
    message_content: str | None
    alias_ingroup: str | None
    group_description: str | None
    group_tab_content: str | None
    file_name: str | None
    file_key: str | None
    document_owner_name: str | None
    document_owner_id: int | None
    document_name: str | None
    document_type: str | None
    document_link: str | None
    evidence_detail: DlpEvidenceDetail | None
    hit_policies: list[DlpHitPolicy] | None
    file_token: str | None
    trigger_event_type: str | None
    chat_type: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DlpExecuteLogBuilder: ...

class DlpExecuteLogBuilder:
    def __init__(self) -> None: ...
    def applicable_service(self, applicable_service: str) -> DlpExecuteLogBuilder: ...
    def user_name(self, user_name: str) -> DlpExecuteLogBuilder: ...
    def user_id(self, user_id: int) -> DlpExecuteLogBuilder: ...
    def trigger(self, trigger: str) -> DlpExecuteLogBuilder: ...
    def time(self, time: int) -> DlpExecuteLogBuilder: ...
    def system_action(self, system_action: str) -> DlpExecuteLogBuilder: ...
    def sender_name(self, sender_name: str) -> DlpExecuteLogBuilder: ...
    def sender_id(self, sender_id: int) -> DlpExecuteLogBuilder: ...
    def recipient_name(self, recipient_name: str) -> DlpExecuteLogBuilder: ...
    def recipient_id(self, recipient_id: int) -> DlpExecuteLogBuilder: ...
    def chat_name(self, chat_name: str) -> DlpExecuteLogBuilder: ...
    def chat_id(self, chat_id: int) -> DlpExecuteLogBuilder: ...
    def message_id(self, message_id: int) -> DlpExecuteLogBuilder: ...
    def message_content(self, message_content: str) -> DlpExecuteLogBuilder: ...
    def alias_ingroup(self, alias_ingroup: str) -> DlpExecuteLogBuilder: ...
    def group_description(self, group_description: str) -> DlpExecuteLogBuilder: ...
    def group_tab_content(self, group_tab_content: str) -> DlpExecuteLogBuilder: ...
    def file_name(self, file_name: str) -> DlpExecuteLogBuilder: ...
    def file_key(self, file_key: str) -> DlpExecuteLogBuilder: ...
    def document_owner_name(self, document_owner_name: str) -> DlpExecuteLogBuilder: ...
    def document_owner_id(self, document_owner_id: int) -> DlpExecuteLogBuilder: ...
    def document_name(self, document_name: str) -> DlpExecuteLogBuilder: ...
    def document_type(self, document_type: str) -> DlpExecuteLogBuilder: ...
    def document_link(self, document_link: str) -> DlpExecuteLogBuilder: ...
    def evidence_detail(self, evidence_detail: DlpEvidenceDetail) -> DlpExecuteLogBuilder: ...
    def hit_policies(self, hit_policies: list[DlpHitPolicy]) -> DlpExecuteLogBuilder: ...
    def file_token(self, file_token: str) -> DlpExecuteLogBuilder: ...
    def trigger_event_type(self, trigger_event_type: str) -> DlpExecuteLogBuilder: ...
    def chat_type(self, chat_type: int) -> DlpExecuteLogBuilder: ...
    def build(self) -> DlpExecuteLog: ...
