from .resource import *

class V1:
    image: Image
    okr: Okr
    period: Period
    period_rule: PeriodRule
    progress_record: ProgressRecord
    review: Review
    user_okr: UserOkr
    def __init__(self, config: Config) -> None: ...
