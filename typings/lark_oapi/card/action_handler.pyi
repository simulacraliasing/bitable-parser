from lark_oapi.core.const import *
from .model import Card as Card
from lark_oapi.core.enum import LogLevel as LogLevel
from lark_oapi.core.exception import AccessDeniedException as AccessDeniedException, CardException as CardException, InvalidArgsException as InvalidArgsException, NoAuthorizationException as NoAuthorizationException
from lark_oapi.core.http import HttpHandler as HttpHandler
from lark_oapi.core.json import JSON as JSON
from lark_oapi.core.log import logger as logger
from lark_oapi.core.model import RawRequest as RawRequest, RawResponse as RawResponse
from lark_oapi.core.utils import AESCipher as AESCipher, Strings as Strings
from typing import Any, Callable

class CardActionHandler(HttpHandler):
    def __init__(self) -> None: ...
    def do(self, req: RawRequest) -> RawResponse: ...
    @staticmethod
    def builder(encrypt_key: str, verification_token: str, level: LogLevel = None) -> CardActionHandlerBuilder: ...

class CardActionHandlerBuilder:
    def __init__(self, encrypt_key: str, verification_token: str) -> None: ...
    def register(self, f: Callable[[Card], Any]) -> CardActionHandlerBuilder: ...
    def build(self) -> CardActionHandler: ...
