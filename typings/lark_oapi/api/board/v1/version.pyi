from .resource import *

class V1:
    whiteboard: Whiteboard
    whiteboard_node: WhiteboardNode
    def __init__(self, config: Config) -> None: ...
