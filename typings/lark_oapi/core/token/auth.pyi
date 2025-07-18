from lark_oapi.core.model import *
from .manager import TokenManager as TokenManager
from lark_oapi.core.exception import NoAuthorizationException as NoAuthorizationException
from lark_oapi.core.utils import Strings as Strings

def verify(config: Config, request: BaseRequest, option: RequestOption) -> None: ...
