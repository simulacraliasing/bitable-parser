from lark_oapi.core.construct import init as init

class Agenda:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AgendaBuilder: ...

class AgendaBuilder:
    def __init__(self) -> None: ...
    def build(self) -> Agenda: ...
