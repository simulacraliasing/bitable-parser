from .resource import *

class V4:
    approval: Approval
    external_approval: ExternalApproval
    external_instance: ExternalInstance
    external_task: ExternalTask
    instance: Instance
    instance_comment: InstanceComment
    task: Task
    def __init__(self, config: Config) -> None: ...
