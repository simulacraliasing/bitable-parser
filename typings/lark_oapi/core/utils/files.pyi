from lark_oapi.core import Content_Disposition as Content_Disposition
from typing import Any

class Files:
    @staticmethod
    def parse_file_name(headers: dict[str, str]) -> str | None: ...
    @staticmethod
    def parse_form_data(obj: Any) -> dict[str, Any]: ...
    @staticmethod
    def extract_files(obj: Any): ...
