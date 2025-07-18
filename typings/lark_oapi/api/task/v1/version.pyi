from .resource import *

class V1:
    task: Task
    task_collaborator: TaskCollaborator
    task_comment: TaskComment
    task_follower: TaskFollower
    task_reminder: TaskReminder
    def __init__(self, config: Config) -> None: ...
