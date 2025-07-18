import shlex
from datetime import datetime
from typing import Any

from lark_oapi.api.bitable.v1 import AppTableFieldForList, Condition, FilterInfo


def parse_filter(filter_str: str):
    filter_str = filter_str.strip()

    # Determine conjunction type
    conjunction, conditions = split_conjunctions(filter_str)

    conditions = [parse_condition(cond) for cond in conditions]

    return FilterInfo.builder().conjunction(conjunction).conditions(conditions).build()


def split_conjunctions(filter_str: str) -> tuple[str, list[str]]:
    for conj in [" and ", " or "]:
        if conj in filter_str:
            parts = filter_str.split(conj)
            return conj.strip(), [p.strip() for p in parts]
    return "and", [filter_str]  # default to AND for single conditions


def parse_condition(cond_str: str):
    tokens = shlex.split(cond_str, posix=False)
    if not tokens:
        raise ValueError("Empty condition")

    field = tokens[0]
    remaining = tokens[1:]

    op_map = {
        "==": "is",
        "!=": "isNot",
        ">": "isGreater",
        ">=": "isGreaterEqual",
        "<": "isLess",
        "<=": "isLessEqual",
        "contain": "contains",
        "not contain": "doesNotContain",
        "is null": "isEmpty",
        "is not null": "isNotEmpty",
    }

    # Extract operator and value
    operator, value = None, []
    for op_pattern in ["is not null", "is null", "not contain"]:
        if " ".join(remaining[: len(op_pattern.split())]) == op_pattern:
            operator = op_pattern
            remaining = remaining[len(op_pattern.split()) :]
            break

    if not operator:  # Check single-token operators
        if remaining:
            operator = remaining[0]
            remaining = remaining[1:]

    if operator not in op_map:
        raise ValueError(f"Invalid operator: {operator}")

    # Handle value for operators that need it
    if operator not in ["is null", "is not null"]:
        if remaining:
            value = [remaining[0]]
        elif op_map[operator] not in ["isEmpty", "isNotEmpty"]:
            raise ValueError(f"Missing value for operator: {operator}")

    return Condition.builder().field_name(field).operator(op_map[operator]).value(value).build()


class RecordParser:
    def __init__(self, field: AppTableFieldForList):
        self.field = field

    def router(self, record: Any):
        match self.field.ui_type:
            case "Text":
                return self.parse_multiline(record)
            case "Number":
                return self.parse_number(record)
            case "Checkbox":
                return self.parse_checkbox(record)
            case "SingleSelect":
                return self.parse_single_option(record)
            case "MultiSelect":
                return self.parse_multiple_option(record)
            case "Url":
                return self.parse_link(record)
            case "SingleLink":
                return self.parse_oneway_link(record)
            case "DuplexLink":
                return self.parse_twoway_link(record)
            case "DateTime":
                return self.parse_date(record)
            case "Progress":
                return self.parse_progress(record)
            case _:
                raise ValueError(f"Invalid field type: {self.field.ui_type}")

    def parse(self, record: Any):
        if record is None:
            return None
        return self.router(record)

    def parse_multiline(self, record: list[dict[str, Any]]) -> str:
        parsed_record: list[str] = []
        for r in record:
            if r["type"] == "text":
                parsed_record.append(r["text"])
            else:
                raise ValueError(f"Invalid record type: {r['type']}, {r}")

        return "".join(parsed_record)

    def parse_number(self, record: str | float) -> float:
        return float(record)

    def parse_checkbox(self, record: bool) -> bool:
        return record

    def parse_single_option(self, record: str) -> str:
        return record

    def parse_multiple_option(self, record: list[str]) -> str:
        return ";".join(record)

    def parse_link(self, record: dict[str, Any]) -> str:
        return record["link"]

    def parse_oneway_link(self, record: dict[str, Any]) -> str:
        links: list[str] = []
        if self.field.property is None:
            return ""
        table_id = self.field.property.table_id
        link_record_ids: list[str] = record["link_record_ids"] if "link_record_ids" in record else []
        for link_record_id in link_record_ids:
            links.append(f"{table_id}:{link_record_id}")
        return ";".join(links)

    def parse_twoway_link(self, record: dict[str, Any]) -> str:
        links: list[str] = []
        if self.field.property is None:
            return ""
        table_id = self.field.property.table_id
        link_record_ids: list[str] = record["link_record_ids"] if "link_record_ids" in record else []
        for link_record_id in link_record_ids:
            links.append(f"{table_id}:{link_record_id}")
        return ";".join(links)

    def parse_date(self, record: int) -> str:
        if self.field.property is None:
            return ""
        format = self.field.property.date_formatter
        if format is None:
            return ""
        format = format.replace("yyyy", "%Y")
        format = format.replace("MM", "%m")
        format = format.replace("dd", "%d")
        format = format.replace("HH", "%H")
        format = format.replace("mm", "%M")
        dt = datetime.fromtimestamp(record / 1000)
        return dt.strftime(format)

    def parse_progress(self, record: str | float) -> float:
        return float(record)
