from .resource import *

class V1:
    batch_message: BatchMessage
    chat: Chat
    chat_access_event: ChatAccessEvent
    chat_announcement: ChatAnnouncement
    chat_managers: ChatManagers
    chat_member_bot: ChatMemberBot
    chat_member_user: ChatMemberUser
    chat_members: ChatMembers
    chat_menu_item: ChatMenuItem
    chat_menu_tree: ChatMenuTree
    chat_moderation: ChatModeration
    chat_tab: ChatTab
    chat_top_notice: ChatTopNotice
    file: File
    image: Image
    message: Message
    message_reaction: MessageReaction
    message_resource: MessageResource
    pin: Pin
    thread: Thread
    def __init__(self, config: Config) -> None: ...
