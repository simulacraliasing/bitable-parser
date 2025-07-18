from .resource import *

class V6:
    app_badge: AppBadge
    app_recommend_rule: AppRecommendRule
    application: Application
    application_app_usage: ApplicationAppUsage
    application_app_version: ApplicationAppVersion
    application_collaborators: ApplicationCollaborators
    application_contacts_range: ApplicationContactsRange
    application_feedback: ApplicationFeedback
    application_management: ApplicationManagement
    application_owner: ApplicationOwner
    application_visibility: ApplicationVisibility
    bot: Bot
    scope: Scope
    def __init__(self, config: Config) -> None: ...
