from .i18n_names import I18nNames as I18nNames
from .restricted_mode_setting import RestrictedModeSetting as RestrictedModeSetting
from lark_oapi.core.construct import init as init

class CreateChatResponseBody:
    chat_id: str | None
    avatar: str | None
    name: str | None
    description: str | None
    i18n_names: I18nNames | None
    owner_id: str | None
    owner_id_type: str | None
    urgent_setting: str | None
    video_conference_setting: str | None
    pin_manage_setting: str | None
    add_member_permission: str | None
    share_card_permission: str | None
    at_all_permission: str | None
    edit_permission: str | None
    group_message_type: str | None
    chat_mode: str | None
    chat_type: str | None
    chat_tag: str | None
    external: bool | None
    tenant_key: str | None
    join_message_visibility: str | None
    leave_message_visibility: str | None
    membership_approval: str | None
    moderation_permission: str | None
    labels: list[str] | None
    toolkit_ids: list[int] | None
    restricted_mode_setting: RestrictedModeSetting | None
    hide_member_count_setting: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateChatResponseBodyBuilder: ...

class CreateChatResponseBodyBuilder:
    def __init__(self) -> None: ...
    def chat_id(self, chat_id: str) -> CreateChatResponseBodyBuilder: ...
    def avatar(self, avatar: str) -> CreateChatResponseBodyBuilder: ...
    def name(self, name: str) -> CreateChatResponseBodyBuilder: ...
    def description(self, description: str) -> CreateChatResponseBodyBuilder: ...
    def i18n_names(self, i18n_names: I18nNames) -> CreateChatResponseBodyBuilder: ...
    def owner_id(self, owner_id: str) -> CreateChatResponseBodyBuilder: ...
    def owner_id_type(self, owner_id_type: str) -> CreateChatResponseBodyBuilder: ...
    def urgent_setting(self, urgent_setting: str) -> CreateChatResponseBodyBuilder: ...
    def video_conference_setting(self, video_conference_setting: str) -> CreateChatResponseBodyBuilder: ...
    def pin_manage_setting(self, pin_manage_setting: str) -> CreateChatResponseBodyBuilder: ...
    def add_member_permission(self, add_member_permission: str) -> CreateChatResponseBodyBuilder: ...
    def share_card_permission(self, share_card_permission: str) -> CreateChatResponseBodyBuilder: ...
    def at_all_permission(self, at_all_permission: str) -> CreateChatResponseBodyBuilder: ...
    def edit_permission(self, edit_permission: str) -> CreateChatResponseBodyBuilder: ...
    def group_message_type(self, group_message_type: str) -> CreateChatResponseBodyBuilder: ...
    def chat_mode(self, chat_mode: str) -> CreateChatResponseBodyBuilder: ...
    def chat_type(self, chat_type: str) -> CreateChatResponseBodyBuilder: ...
    def chat_tag(self, chat_tag: str) -> CreateChatResponseBodyBuilder: ...
    def external(self, external: bool) -> CreateChatResponseBodyBuilder: ...
    def tenant_key(self, tenant_key: str) -> CreateChatResponseBodyBuilder: ...
    def join_message_visibility(self, join_message_visibility: str) -> CreateChatResponseBodyBuilder: ...
    def leave_message_visibility(self, leave_message_visibility: str) -> CreateChatResponseBodyBuilder: ...
    def membership_approval(self, membership_approval: str) -> CreateChatResponseBodyBuilder: ...
    def moderation_permission(self, moderation_permission: str) -> CreateChatResponseBodyBuilder: ...
    def labels(self, labels: list[str]) -> CreateChatResponseBodyBuilder: ...
    def toolkit_ids(self, toolkit_ids: list[int]) -> CreateChatResponseBodyBuilder: ...
    def restricted_mode_setting(self, restricted_mode_setting: RestrictedModeSetting) -> CreateChatResponseBodyBuilder: ...
    def hide_member_count_setting(self, hide_member_count_setting: str) -> CreateChatResponseBodyBuilder: ...
    def build(self) -> CreateChatResponseBody: ...
