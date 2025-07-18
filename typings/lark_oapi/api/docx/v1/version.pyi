from .resource import *

class V1:
    chat_announcement: ChatAnnouncement
    chat_announcement_block: ChatAnnouncementBlock
    chat_announcement_block_children: ChatAnnouncementBlockChildren
    document: Document
    document_block: DocumentBlock
    document_block_children: DocumentBlockChildren
    document_block_descendant: DocumentBlockDescendant
    def __init__(self, config: Config) -> None: ...
