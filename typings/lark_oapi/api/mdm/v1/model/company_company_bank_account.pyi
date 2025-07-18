from .i18n_struct import I18nStruct as I18nStruct
from lark_oapi.core.construct import init as init

class CompanyCompanyBankAccount:
    company_bank_account_uid: str | None
    company_uid: str | None
    account: str | None
    iban: str | None
    account_name: str | None
    currency_code: str | None
    local_routing_code: str | None
    gl_account_code: str | None
    clearing_account_code: str | None
    swift: str | None
    account_attri_desc: str | None
    i18n_account_attri_desc: list[I18nStruct] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CompanyCompanyBankAccountBuilder: ...

class CompanyCompanyBankAccountBuilder:
    def __init__(self) -> None: ...
    def company_bank_account_uid(self, company_bank_account_uid: str) -> CompanyCompanyBankAccountBuilder: ...
    def company_uid(self, company_uid: str) -> CompanyCompanyBankAccountBuilder: ...
    def account(self, account: str) -> CompanyCompanyBankAccountBuilder: ...
    def iban(self, iban: str) -> CompanyCompanyBankAccountBuilder: ...
    def account_name(self, account_name: str) -> CompanyCompanyBankAccountBuilder: ...
    def currency_code(self, currency_code: str) -> CompanyCompanyBankAccountBuilder: ...
    def local_routing_code(self, local_routing_code: str) -> CompanyCompanyBankAccountBuilder: ...
    def gl_account_code(self, gl_account_code: str) -> CompanyCompanyBankAccountBuilder: ...
    def clearing_account_code(self, clearing_account_code: str) -> CompanyCompanyBankAccountBuilder: ...
    def swift(self, swift: str) -> CompanyCompanyBankAccountBuilder: ...
    def account_attri_desc(self, account_attri_desc: str) -> CompanyCompanyBankAccountBuilder: ...
    def i18n_account_attri_desc(self, i18n_account_attri_desc: list[I18nStruct]) -> CompanyCompanyBankAccountBuilder: ...
    def build(self) -> CompanyCompanyBankAccount: ...
