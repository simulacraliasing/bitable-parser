from lark_oapi.core.const import *
from lark_oapi.core.model import *
from lark_oapi.core.json import JSON as JSON
from lark_oapi.core.log import logger as logger

class Transport:
    @staticmethod
    def execute(conf: Config, req: BaseRequest, option: Optional[RequestOption] = None) -> RawResponse: ...
    @staticmethod
    async def aexecute(conf: Config, req: BaseRequest, option: Optional[RequestOption] = None) -> RawResponse: ...
