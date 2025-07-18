from .resource import *

class V1:
    app: App
    app_dashboard: AppDashboard
    app_role: AppRole
    app_role_member: AppRoleMember
    app_table: AppTable
    app_table_field: AppTableField
    app_table_form: AppTableForm
    app_table_form_field: AppTableFormField
    app_table_record: AppTableRecord
    app_table_view: AppTableView
    app_workflow: AppWorkflow
    def __init__(self, config: Config) -> None: ...
