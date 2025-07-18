from lark_oapi.core.construct import init as init

class DepartmentI18nName:
    zh_cn: str | None
    ja_jp: str | None
    en_us: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DepartmentI18nNameBuilder: ...

class DepartmentI18nNameBuilder:
    def __init__(self) -> None: ...
    def zh_cn(self, zh_cn: str) -> DepartmentI18nNameBuilder: ...
    def ja_jp(self, ja_jp: str) -> DepartmentI18nNameBuilder: ...
    def en_us(self, en_us: str) -> DepartmentI18nNameBuilder: ...
    def build(self) -> DepartmentI18nName: ...
