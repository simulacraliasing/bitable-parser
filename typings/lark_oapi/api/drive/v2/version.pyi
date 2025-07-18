from .resource import *

class V2:
    file_like: FileLike
    permission_public: PermissionPublic
    def __init__(self, config: Config) -> None: ...
