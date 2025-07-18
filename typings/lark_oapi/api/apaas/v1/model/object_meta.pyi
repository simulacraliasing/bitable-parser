from .object import Object as Object
from .object_field import ObjectField as ObjectField
from lark_oapi.core.construct import init as init

class ObjectMeta:
    object: Object | None
    fields: list[ObjectField] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ObjectMetaBuilder: ...

class ObjectMetaBuilder:
    def __init__(self) -> None: ...
    def object(self, object: Object) -> ObjectMetaBuilder: ...
    def fields(self, fields: list[ObjectField]) -> ObjectMetaBuilder: ...
    def build(self) -> ObjectMeta: ...
