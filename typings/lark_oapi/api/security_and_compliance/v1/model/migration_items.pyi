from .migration_entity import MigrationEntity as MigrationEntity
from lark_oapi.core.construct import init as init

class MigrationItems:
    task_id: str | None
    task_status: str | None
    entity: MigrationEntity | None
    message: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MigrationItemsBuilder: ...

class MigrationItemsBuilder:
    def __init__(self) -> None: ...
    def task_id(self, task_id: str) -> MigrationItemsBuilder: ...
    def task_status(self, task_status: str) -> MigrationItemsBuilder: ...
    def entity(self, entity: MigrationEntity) -> MigrationItemsBuilder: ...
    def message(self, message: str) -> MigrationItemsBuilder: ...
    def build(self) -> MigrationItems: ...
