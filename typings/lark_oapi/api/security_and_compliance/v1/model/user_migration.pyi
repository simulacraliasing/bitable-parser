from lark_oapi.core.construct import init as init

class UserMigration:
    user_id: int | None
    dest_geo: str | None
    task_id: str | None
    status: str | None
    progress: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UserMigrationBuilder: ...

class UserMigrationBuilder:
    def __init__(self) -> None: ...
    def user_id(self, user_id: int) -> UserMigrationBuilder: ...
    def dest_geo(self, dest_geo: str) -> UserMigrationBuilder: ...
    def task_id(self, task_id: str) -> UserMigrationBuilder: ...
    def status(self, status: str) -> UserMigrationBuilder: ...
    def progress(self, progress: int) -> UserMigrationBuilder: ...
    def build(self) -> UserMigration: ...
