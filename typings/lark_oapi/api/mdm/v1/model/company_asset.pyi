from lark_oapi.core.construct import init as init

class CompanyAsset:
    asset_uid: str | None
    asset_sub_no: str | None
    asset_type: str | None
    asset_type_name: str | None
    asset_name: str | None
    quantity: int | None
    unit: str | None
    company_uid: str | None
    asset_type_name_en: str | None
    asset_no: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CompanyAssetBuilder: ...

class CompanyAssetBuilder:
    def __init__(self) -> None: ...
    def asset_uid(self, asset_uid: str) -> CompanyAssetBuilder: ...
    def asset_sub_no(self, asset_sub_no: str) -> CompanyAssetBuilder: ...
    def asset_type(self, asset_type: str) -> CompanyAssetBuilder: ...
    def asset_type_name(self, asset_type_name: str) -> CompanyAssetBuilder: ...
    def asset_name(self, asset_name: str) -> CompanyAssetBuilder: ...
    def quantity(self, quantity: int) -> CompanyAssetBuilder: ...
    def unit(self, unit: str) -> CompanyAssetBuilder: ...
    def company_uid(self, company_uid: str) -> CompanyAssetBuilder: ...
    def asset_type_name_en(self, asset_type_name_en: str) -> CompanyAssetBuilder: ...
    def asset_no(self, asset_no: str) -> CompanyAssetBuilder: ...
    def build(self) -> CompanyAsset: ...
