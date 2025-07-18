from .onboarding_flow import OnboardingFlow as OnboardingFlow
from .onboarding_flow_change import OnboardingFlowChange as OnboardingFlowChange
from .onboarding_task_change import OnboardingTaskChange as OnboardingTaskChange
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrPreHireOnboardingTaskChangedV2Data:
    tenant_id: str | None
    pre_hire_id: str | None
    onboarding_task_changes: list[OnboardingTaskChange] | None
    onboarding_flow_change: OnboardingFlowChange | None
    onboarding_flow_id: str | None
    flow_info: OnboardingFlow | None
    def __init__(self, d=None) -> None: ...

class P2CorehrPreHireOnboardingTaskChangedV2(EventContext):
    event: P2CorehrPreHireOnboardingTaskChangedV2Data | None
    def __init__(self, d=None) -> None: ...
