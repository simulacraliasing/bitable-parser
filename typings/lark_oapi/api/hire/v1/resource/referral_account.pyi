from ..model.create_referral_account_request import CreateReferralAccountRequest as CreateReferralAccountRequest
from ..model.create_referral_account_response import CreateReferralAccountResponse as CreateReferralAccountResponse
from ..model.deactivate_referral_account_request import DeactivateReferralAccountRequest as DeactivateReferralAccountRequest
from ..model.deactivate_referral_account_response import DeactivateReferralAccountResponse as DeactivateReferralAccountResponse
from ..model.enable_referral_account_request import EnableReferralAccountRequest as EnableReferralAccountRequest
from ..model.enable_referral_account_response import EnableReferralAccountResponse as EnableReferralAccountResponse
from ..model.get_account_assets_referral_account_request import GetAccountAssetsReferralAccountRequest as GetAccountAssetsReferralAccountRequest
from ..model.get_account_assets_referral_account_response import GetAccountAssetsReferralAccountResponse as GetAccountAssetsReferralAccountResponse
from ..model.reconciliation_referral_account_request import ReconciliationReferralAccountRequest as ReconciliationReferralAccountRequest
from ..model.reconciliation_referral_account_response import ReconciliationReferralAccountResponse as ReconciliationReferralAccountResponse
from ..model.withdraw_referral_account_request import WithdrawReferralAccountRequest as WithdrawReferralAccountRequest
from ..model.withdraw_referral_account_response import WithdrawReferralAccountResponse as WithdrawReferralAccountResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ReferralAccount:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateReferralAccountRequest, option: RequestOption | None = None) -> CreateReferralAccountResponse: ...
    async def acreate(self, request: CreateReferralAccountRequest, option: RequestOption | None = None) -> CreateReferralAccountResponse: ...
    def deactivate(self, request: DeactivateReferralAccountRequest, option: RequestOption | None = None) -> DeactivateReferralAccountResponse: ...
    async def adeactivate(self, request: DeactivateReferralAccountRequest, option: RequestOption | None = None) -> DeactivateReferralAccountResponse: ...
    def enable(self, request: EnableReferralAccountRequest, option: RequestOption | None = None) -> EnableReferralAccountResponse: ...
    async def aenable(self, request: EnableReferralAccountRequest, option: RequestOption | None = None) -> EnableReferralAccountResponse: ...
    def get_account_assets(self, request: GetAccountAssetsReferralAccountRequest, option: RequestOption | None = None) -> GetAccountAssetsReferralAccountResponse: ...
    async def aget_account_assets(self, request: GetAccountAssetsReferralAccountRequest, option: RequestOption | None = None) -> GetAccountAssetsReferralAccountResponse: ...
    def reconciliation(self, request: ReconciliationReferralAccountRequest, option: RequestOption | None = None) -> ReconciliationReferralAccountResponse: ...
    async def areconciliation(self, request: ReconciliationReferralAccountRequest, option: RequestOption | None = None) -> ReconciliationReferralAccountResponse: ...
    def withdraw(self, request: WithdrawReferralAccountRequest, option: RequestOption | None = None) -> WithdrawReferralAccountResponse: ...
    async def awithdraw(self, request: WithdrawReferralAccountRequest, option: RequestOption | None = None) -> WithdrawReferralAccountResponse: ...
