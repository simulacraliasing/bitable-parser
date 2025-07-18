from lark_oapi.core.construct import init as init

class SearchOffboardingRequestBody:
    employment_ids: list[str] | None
    apply_initiating_time_start: str | None
    apply_initiating_time_end: str | None
    apply_finished_time_start: str | None
    apply_finished_time_end: str | None
    expected_offboarding_date_start: str | None
    expected_offboarding_date_end: str | None
    offboarding_date_start: str | None
    offboarding_date_end: str | None
    statuses: list[str] | None
    reasons: list[str] | None
    employee_reasons: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SearchOffboardingRequestBodyBuilder: ...

class SearchOffboardingRequestBodyBuilder:
    def __init__(self) -> None: ...
    def employment_ids(self, employment_ids: list[str]) -> SearchOffboardingRequestBodyBuilder: ...
    def apply_initiating_time_start(self, apply_initiating_time_start: str) -> SearchOffboardingRequestBodyBuilder: ...
    def apply_initiating_time_end(self, apply_initiating_time_end: str) -> SearchOffboardingRequestBodyBuilder: ...
    def apply_finished_time_start(self, apply_finished_time_start: str) -> SearchOffboardingRequestBodyBuilder: ...
    def apply_finished_time_end(self, apply_finished_time_end: str) -> SearchOffboardingRequestBodyBuilder: ...
    def expected_offboarding_date_start(self, expected_offboarding_date_start: str) -> SearchOffboardingRequestBodyBuilder: ...
    def expected_offboarding_date_end(self, expected_offboarding_date_end: str) -> SearchOffboardingRequestBodyBuilder: ...
    def offboarding_date_start(self, offboarding_date_start: str) -> SearchOffboardingRequestBodyBuilder: ...
    def offboarding_date_end(self, offboarding_date_end: str) -> SearchOffboardingRequestBodyBuilder: ...
    def statuses(self, statuses: list[str]) -> SearchOffboardingRequestBodyBuilder: ...
    def reasons(self, reasons: list[str]) -> SearchOffboardingRequestBodyBuilder: ...
    def employee_reasons(self, employee_reasons: list[str]) -> SearchOffboardingRequestBodyBuilder: ...
    def build(self) -> SearchOffboardingRequestBody: ...
