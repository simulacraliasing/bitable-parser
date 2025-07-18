from ..model.batch_delete_eco_background_check_package_request import BatchDeleteEcoBackgroundCheckPackageRequest as BatchDeleteEcoBackgroundCheckPackageRequest
from ..model.batch_delete_eco_background_check_package_response import BatchDeleteEcoBackgroundCheckPackageResponse as BatchDeleteEcoBackgroundCheckPackageResponse
from ..model.batch_update_eco_background_check_package_request import BatchUpdateEcoBackgroundCheckPackageRequest as BatchUpdateEcoBackgroundCheckPackageRequest
from ..model.batch_update_eco_background_check_package_response import BatchUpdateEcoBackgroundCheckPackageResponse as BatchUpdateEcoBackgroundCheckPackageResponse
from ..model.create_eco_background_check_package_request import CreateEcoBackgroundCheckPackageRequest as CreateEcoBackgroundCheckPackageRequest
from ..model.create_eco_background_check_package_response import CreateEcoBackgroundCheckPackageResponse as CreateEcoBackgroundCheckPackageResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class EcoBackgroundCheckPackage:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def batch_delete(self, request: BatchDeleteEcoBackgroundCheckPackageRequest, option: RequestOption | None = None) -> BatchDeleteEcoBackgroundCheckPackageResponse: ...
    async def abatch_delete(self, request: BatchDeleteEcoBackgroundCheckPackageRequest, option: RequestOption | None = None) -> BatchDeleteEcoBackgroundCheckPackageResponse: ...
    def batch_update(self, request: BatchUpdateEcoBackgroundCheckPackageRequest, option: RequestOption | None = None) -> BatchUpdateEcoBackgroundCheckPackageResponse: ...
    async def abatch_update(self, request: BatchUpdateEcoBackgroundCheckPackageRequest, option: RequestOption | None = None) -> BatchUpdateEcoBackgroundCheckPackageResponse: ...
    def create(self, request: CreateEcoBackgroundCheckPackageRequest, option: RequestOption | None = None) -> CreateEcoBackgroundCheckPackageResponse: ...
    async def acreate(self, request: CreateEcoBackgroundCheckPackageRequest, option: RequestOption | None = None) -> CreateEcoBackgroundCheckPackageResponse: ...
