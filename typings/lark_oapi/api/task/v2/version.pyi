from .resource import *

class V2:
    attachment: Attachment
    comment: Comment
    custom_field: CustomField
    custom_field_option: CustomFieldOption
    section: Section
    task: Task
    task_subtask: TaskSubtask
    tasklist: Tasklist
    tasklist_activity_subscription: TasklistActivitySubscription
    def __init__(self, config: Config) -> None: ...
