from json import *
from typing import *
from .const import UTF_8 as UTF_8
from .type import T as T
from typing import Any

class JSON:
    @staticmethod
    def marshal(obj: Any, indent=None) -> Optional[str]: ...
    @staticmethod
    def unmarshal(json_str: str, clazz: Type[T]) -> T: ...

class Encoder(JSONEncoder):
    def default(self, o: Any) -> Any: ...

def filter_null(d: Dict) -> Dict: ...
