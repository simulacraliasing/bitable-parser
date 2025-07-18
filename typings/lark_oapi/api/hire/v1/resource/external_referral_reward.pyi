from ..model.create_external_referral_reward_request import CreateExternalReferralRewardRequest as CreateExternalReferralRewardRequest
from ..model.create_external_referral_reward_response import CreateExternalReferralRewardResponse as CreateExternalReferralRewardResponse
from ..model.delete_external_referral_reward_request import DeleteExternalReferralRewardRequest as DeleteExternalReferralRewardRequest
from ..model.delete_external_referral_reward_response import DeleteExternalReferralRewardResponse as DeleteExternalReferralRewardResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ExternalReferralReward:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateExternalReferralRewardRequest, option: RequestOption | None = None) -> CreateExternalReferralRewardResponse: ...
    async def acreate(self, request: CreateExternalReferralRewardRequest, option: RequestOption | None = None) -> CreateExternalReferralRewardResponse: ...
    def delete(self, request: DeleteExternalReferralRewardRequest, option: RequestOption | None = None) -> DeleteExternalReferralRewardResponse: ...
    async def adelete(self, request: DeleteExternalReferralRewardRequest, option: RequestOption | None = None) -> DeleteExternalReferralRewardResponse: ...
