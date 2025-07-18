from .resource import *

class V1:
    mailgroup: Mailgroup
    mailgroup_alias: MailgroupAlias
    mailgroup_manager: MailgroupManager
    mailgroup_member: MailgroupMember
    mailgroup_permission_member: MailgroupPermissionMember
    public_mailbox: PublicMailbox
    public_mailbox_alias: PublicMailboxAlias
    public_mailbox_member: PublicMailboxMember
    user: User
    user_mailbox: UserMailbox
    user_mailbox_alias: UserMailboxAlias
    user_mailbox_event: UserMailboxEvent
    user_mailbox_folder: UserMailboxFolder
    user_mailbox_mail_contact: UserMailboxMailContact
    user_mailbox_message: UserMailboxMessage
    user_mailbox_message_attachment: UserMailboxMessageAttachment
    user_mailbox_rule: UserMailboxRule
    def __init__(self, config: Config) -> None: ...
