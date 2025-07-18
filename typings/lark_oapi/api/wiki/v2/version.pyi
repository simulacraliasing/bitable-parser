from .resource import *

class V2:
    space: Space
    space_member: SpaceMember
    space_node: SpaceNode
    space_setting: SpaceSetting
    task: Task
    def __init__(self, config: Config) -> None: ...
