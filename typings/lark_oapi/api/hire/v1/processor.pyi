from .model.p2_hire_application_deleted_v1 import P2HireApplicationDeletedV1 as P2HireApplicationDeletedV1
from .model.p2_hire_application_stage_changed_v1 import P2HireApplicationStageChangedV1 as P2HireApplicationStageChangedV1
from .model.p2_hire_eco_account_created_v1 import P2HireEcoAccountCreatedV1 as P2HireEcoAccountCreatedV1
from .model.p2_hire_eco_background_check_canceled_v1 import P2HireEcoBackgroundCheckCanceledV1 as P2HireEcoBackgroundCheckCanceledV1
from .model.p2_hire_eco_background_check_created_v1 import P2HireEcoBackgroundCheckCreatedV1 as P2HireEcoBackgroundCheckCreatedV1
from .model.p2_hire_eco_exam_created_v1 import P2HireEcoExamCreatedV1 as P2HireEcoExamCreatedV1
from .model.p2_hire_ehr_import_task_for_internship_offer_imported_v1 import P2HireEhrImportTaskForInternshipOfferImportedV1 as P2HireEhrImportTaskForInternshipOfferImportedV1
from .model.p2_hire_ehr_import_task_imported_v1 import P2HireEhrImportTaskImportedV1 as P2HireEhrImportTaskImportedV1
from .model.p2_hire_offer_status_changed_v1 import P2HireOfferStatusChangedV1 as P2HireOfferStatusChangedV1
from .model.p2_hire_referral_account_assets_update_v1 import P2HireReferralAccountAssetsUpdateV1 as P2HireReferralAccountAssetsUpdateV1
from .model.p2_hire_talent_deleted_v1 import P2HireTalentDeletedV1 as P2HireTalentDeletedV1
from .model.p2_hire_talent_tag_subscription_v1 import P2HireTalentTagSubscriptionV1 as P2HireTalentTagSubscriptionV1
from _typeshed import Incomplete
from lark_oapi.event.processor import IEventProcessor as IEventProcessor
from typing import Callable

class P2HireApplicationDeletedV1Processor(IEventProcessor[P2HireApplicationDeletedV1]):
    f: Incomplete
    def __init__(self, f: Callable[[P2HireApplicationDeletedV1], None]) -> None: ...
    def type(self) -> type[P2HireApplicationDeletedV1]: ...
    def do(self, data: P2HireApplicationDeletedV1) -> None: ...

class P2HireApplicationStageChangedV1Processor(IEventProcessor[P2HireApplicationStageChangedV1]):
    f: Incomplete
    def __init__(self, f: Callable[[P2HireApplicationStageChangedV1], None]) -> None: ...
    def type(self) -> type[P2HireApplicationStageChangedV1]: ...
    def do(self, data: P2HireApplicationStageChangedV1) -> None: ...

class P2HireEcoAccountCreatedV1Processor(IEventProcessor[P2HireEcoAccountCreatedV1]):
    f: Incomplete
    def __init__(self, f: Callable[[P2HireEcoAccountCreatedV1], None]) -> None: ...
    def type(self) -> type[P2HireEcoAccountCreatedV1]: ...
    def do(self, data: P2HireEcoAccountCreatedV1) -> None: ...

class P2HireEcoBackgroundCheckCanceledV1Processor(IEventProcessor[P2HireEcoBackgroundCheckCanceledV1]):
    f: Incomplete
    def __init__(self, f: Callable[[P2HireEcoBackgroundCheckCanceledV1], None]) -> None: ...
    def type(self) -> type[P2HireEcoBackgroundCheckCanceledV1]: ...
    def do(self, data: P2HireEcoBackgroundCheckCanceledV1) -> None: ...

class P2HireEcoBackgroundCheckCreatedV1Processor(IEventProcessor[P2HireEcoBackgroundCheckCreatedV1]):
    f: Incomplete
    def __init__(self, f: Callable[[P2HireEcoBackgroundCheckCreatedV1], None]) -> None: ...
    def type(self) -> type[P2HireEcoBackgroundCheckCreatedV1]: ...
    def do(self, data: P2HireEcoBackgroundCheckCreatedV1) -> None: ...

class P2HireEcoExamCreatedV1Processor(IEventProcessor[P2HireEcoExamCreatedV1]):
    f: Incomplete
    def __init__(self, f: Callable[[P2HireEcoExamCreatedV1], None]) -> None: ...
    def type(self) -> type[P2HireEcoExamCreatedV1]: ...
    def do(self, data: P2HireEcoExamCreatedV1) -> None: ...

class P2HireEhrImportTaskImportedV1Processor(IEventProcessor[P2HireEhrImportTaskImportedV1]):
    f: Incomplete
    def __init__(self, f: Callable[[P2HireEhrImportTaskImportedV1], None]) -> None: ...
    def type(self) -> type[P2HireEhrImportTaskImportedV1]: ...
    def do(self, data: P2HireEhrImportTaskImportedV1) -> None: ...

class P2HireEhrImportTaskForInternshipOfferImportedV1Processor(IEventProcessor[P2HireEhrImportTaskForInternshipOfferImportedV1]):
    f: Incomplete
    def __init__(self, f: Callable[[P2HireEhrImportTaskForInternshipOfferImportedV1], None]) -> None: ...
    def type(self) -> type[P2HireEhrImportTaskForInternshipOfferImportedV1]: ...
    def do(self, data: P2HireEhrImportTaskForInternshipOfferImportedV1) -> None: ...

class P2HireOfferStatusChangedV1Processor(IEventProcessor[P2HireOfferStatusChangedV1]):
    f: Incomplete
    def __init__(self, f: Callable[[P2HireOfferStatusChangedV1], None]) -> None: ...
    def type(self) -> type[P2HireOfferStatusChangedV1]: ...
    def do(self, data: P2HireOfferStatusChangedV1) -> None: ...

class P2HireReferralAccountAssetsUpdateV1Processor(IEventProcessor[P2HireReferralAccountAssetsUpdateV1]):
    f: Incomplete
    def __init__(self, f: Callable[[P2HireReferralAccountAssetsUpdateV1], None]) -> None: ...
    def type(self) -> type[P2HireReferralAccountAssetsUpdateV1]: ...
    def do(self, data: P2HireReferralAccountAssetsUpdateV1) -> None: ...

class P2HireTalentDeletedV1Processor(IEventProcessor[P2HireTalentDeletedV1]):
    f: Incomplete
    def __init__(self, f: Callable[[P2HireTalentDeletedV1], None]) -> None: ...
    def type(self) -> type[P2HireTalentDeletedV1]: ...
    def do(self, data: P2HireTalentDeletedV1) -> None: ...

class P2HireTalentTagSubscriptionV1Processor(IEventProcessor[P2HireTalentTagSubscriptionV1]):
    f: Incomplete
    def __init__(self, f: Callable[[P2HireTalentTagSubscriptionV1], None]) -> None: ...
    def type(self) -> type[P2HireTalentTagSubscriptionV1]: ...
    def do(self, data: P2HireTalentTagSubscriptionV1) -> None: ...
