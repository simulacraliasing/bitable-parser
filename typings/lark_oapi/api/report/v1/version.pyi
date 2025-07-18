from .resource import *

class V1:
    rule: Rule
    rule_view: RuleView
    task: Task
    def __init__(self, config: Config) -> None: ...
