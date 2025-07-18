from .memory_message import MemoryMessage as MemoryMessage
from .scenario_context_extra import ScenarioContextExtra as ScenarioContextExtra
from .system_info import SystemInfo as SystemInfo
from lark_oapi.core.construct import init as init

class ScenarioContext:
    extra: ScenarioContextExtra | None
    system_info: SystemInfo | None
    memory: list[MemoryMessage] | None
    scenario: str | None
    work_mode: int | None
    tool_raw_instruction: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ScenarioContextBuilder: ...

class ScenarioContextBuilder:
    def __init__(self) -> None: ...
    def extra(self, extra: ScenarioContextExtra) -> ScenarioContextBuilder: ...
    def system_info(self, system_info: SystemInfo) -> ScenarioContextBuilder: ...
    def memory(self, memory: list[MemoryMessage]) -> ScenarioContextBuilder: ...
    def scenario(self, scenario: str) -> ScenarioContextBuilder: ...
    def work_mode(self, work_mode: int) -> ScenarioContextBuilder: ...
    def tool_raw_instruction(self, tool_raw_instruction: str) -> ScenarioContextBuilder: ...
    def build(self) -> ScenarioContext: ...
