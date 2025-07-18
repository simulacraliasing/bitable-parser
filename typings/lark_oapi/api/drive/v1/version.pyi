from .resource import *

class V1:
    export_task: ExportTask
    file: File
    file_comment: FileComment
    file_comment_reply: FileCommentReply
    file_statistics: FileStatistics
    file_subscription: FileSubscription
    file_version: FileVersion
    file_view_record: FileViewRecord
    import_task: ImportTask
    media: Media
    meta: Meta
    permission_member: PermissionMember
    permission_public: PermissionPublic
    permission_public_password: PermissionPublicPassword
    def __init__(self, config: Config) -> None: ...
