from lark_oapi.core.construct import init as init

class ApplicationPrehireOptional:
    with_talent_basic: bool | None
    with_talent_extend: bool | None
    with_job: bool | None
    with_offer: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ApplicationPrehireOptionalBuilder: ...

class ApplicationPrehireOptionalBuilder:
    def __init__(self) -> None: ...
    def with_talent_basic(self, with_talent_basic: bool) -> ApplicationPrehireOptionalBuilder: ...
    def with_talent_extend(self, with_talent_extend: bool) -> ApplicationPrehireOptionalBuilder: ...
    def with_job(self, with_job: bool) -> ApplicationPrehireOptionalBuilder: ...
    def with_offer(self, with_offer: bool) -> ApplicationPrehireOptionalBuilder: ...
    def build(self) -> ApplicationPrehireOptional: ...
