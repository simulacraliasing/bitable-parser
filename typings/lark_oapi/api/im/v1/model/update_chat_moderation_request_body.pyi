from lark_oapi.core.construct import init as init

class UpdateChatModerationRequestBody:
    moderation_setting: str | None
    moderator_added_list: list[str] | None
    moderator_removed_list: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UpdateChatModerationRequestBodyBuilder: ...

class UpdateChatModerationRequestBodyBuilder:
    def __init__(self) -> None: ...
    def moderation_setting(self, moderation_setting: str) -> UpdateChatModerationRequestBodyBuilder: ...
    def moderator_added_list(self, moderator_added_list: list[str]) -> UpdateChatModerationRequestBodyBuilder: ...
    def moderator_removed_list(self, moderator_removed_list: list[str]) -> UpdateChatModerationRequestBodyBuilder: ...
    def build(self) -> UpdateChatModerationRequestBody: ...
