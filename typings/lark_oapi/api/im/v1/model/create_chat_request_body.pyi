from .i18n_names import I18nNames as I18nNames
from .restricted_mode_setting import RestrictedModeSetting as RestrictedModeSetting
from lark_oapi.core.construct import init as init

class CreateChatRequestBody:
    avatar: str | None
    name: str | None
    description: str | None
    i18n_names: I18nNames | None
    owner_id: str | None
    user_id_list: list[str] | None
    bot_id_list: list[str] | None
    group_message_type: str | None
    chat_mode: str | None
    chat_type: str | None
    external: bool | None
    join_message_visibility: str | None
    leave_message_visibility: str | None
    membership_approval: str | None
    labels: list[str] | None
    toolkit_ids: list[int] | None
    restricted_mode_setting: RestrictedModeSetting | None
    urgent_setting: str | None
    video_conference_setting: str | None
    edit_permission: str | None
    chat_tags: list[str] | None
    pin_manage_setting: str | None
    hide_member_count_setting: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateChatRequestBodyBuilder: ...

class CreateChatRequestBodyBuilder:
    def __init__(self) -> None: ...
    def avatar(self, avatar: str) -> CreateChatRequestBodyBuilder: ...
    def name(self, name: str) -> CreateChatRequestBodyBuilder: ...
    def description(self, description: str) -> CreateChatRequestBodyBuilder: ...
    def i18n_names(self, i18n_names: I18nNames) -> CreateChatRequestBodyBuilder: ...
    def owner_id(self, owner_id: str) -> CreateChatRequestBodyBuilder: ...
    def user_id_list(self, user_id_list: list[str]) -> CreateChatRequestBodyBuilder: ...
    def bot_id_list(self, bot_id_list: list[str]) -> CreateChatRequestBodyBuilder: ...
    def group_message_type(self, group_message_type: str) -> CreateChatRequestBodyBuilder: ...
    def chat_mode(self, chat_mode: str) -> CreateChatRequestBodyBuilder: ...
    def chat_type(self, chat_type: str) -> CreateChatRequestBodyBuilder: ...
    def external(self, external: bool) -> CreateChatRequestBodyBuilder: ...
    def join_message_visibility(self, join_message_visibility: str) -> CreateChatRequestBodyBuilder: ...
    def leave_message_visibility(self, leave_message_visibility: str) -> CreateChatRequestBodyBuilder: ...
    def membership_approval(self, membership_approval: str) -> CreateChatRequestBodyBuilder: ...
    def labels(self, labels: list[str]) -> CreateChatRequestBodyBuilder: ...
    def toolkit_ids(self, toolkit_ids: list[int]) -> CreateChatRequestBodyBuilder: ...
    def restricted_mode_setting(self, restricted_mode_setting: RestrictedModeSetting) -> CreateChatRequestBodyBuilder: ...
    def urgent_setting(self, urgent_setting: str) -> CreateChatRequestBodyBuilder: ...
    def video_conference_setting(self, video_conference_setting: str) -> CreateChatRequestBodyBuilder: ...
    def edit_permission(self, edit_permission: str) -> CreateChatRequestBodyBuilder: ...
    def chat_tags(self, chat_tags: list[str]) -> CreateChatRequestBodyBuilder: ...
    def pin_manage_setting(self, pin_manage_setting: str) -> CreateChatRequestBodyBuilder: ...
    def hide_member_count_setting(self, hide_member_count_setting: str) -> CreateChatRequestBodyBuilder: ...
    def build(self) -> CreateChatRequestBody: ...
