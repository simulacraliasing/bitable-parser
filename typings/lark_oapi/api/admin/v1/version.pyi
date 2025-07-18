from .resource import *

class V1:
    admin_dept_stat: AdminDeptStat
    admin_user_stat: AdminUserStat
    audit_info: AuditInfo
    badge: Badge
    badge_grant: BadgeGrant
    badge_image: BadgeImage
    password: Password
    def __init__(self, config: Config) -> None: ...
