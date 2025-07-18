from typing import *
from lark_oapi.core.construct import init as init

class ErrorDetail:
    key: Optional[str]
    value: Optional[str]
    def __init__(self, d=None) -> None: ...

class ErrorPermissionViolation:
    type: Optional[str]
    subject: Optional[str]
    description: Optional[str]
    def __init__(self, d=None) -> None: ...

class ErrorFieldViolation:
    field: Optional[str]
    value: Optional[str]
    description: Optional[str]
    def __init__(self, d=None) -> None: ...

class ErrorHelp:
    url: Optional[str]
    description: Optional[str]
    def __init__(self, d=None) -> None: ...

class Error:
    log_id: Optional[str]
    troubleshooter: Optional[str]
    details: Optional[List[ErrorDetail]]
    permission_violations: Optional[List[ErrorPermissionViolation]]
    field_violations: Optional[List[ErrorFieldViolation]]
    helps: Optional[List[ErrorHelp]]
    def __init__(self, d=None) -> None: ...
