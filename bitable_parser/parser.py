from datetime import datetime


class RecordParser:
    def __init__(self, field):
        self.field = field

    def router(self, record):
        if self.field.ui_type == "Text":
            return self.parse_multiline(record)
        elif self.field.ui_type == "Number":
            return self.parse_number(record)
        elif self.field.ui_type == "Checkbox":
            return self.parse_checkbox(record)
        elif self.field.ui_type == "SingleSelect":
            return self.parse_single_option(record)
        elif self.field.ui_type == "MultiSelect":
            return self.parse_multiple_option(record)
        elif self.field.ui_type == "Url":
            return self.parse_link(record)
        elif self.field.ui_type == "SingleLink":
            return self.parse_oneway_link(record)
        elif self.field.ui_type == "DuplexLink":
            return self.parse_twoway_link(record)
        elif self.field.ui_type == "DateTime":
            return self.parse_date(record)
        elif self.field.ui_type == "Progress":
            return self.parse_progress(record)
        else:
            raise ValueError(f"Invalid field type: {self.field.ui_type}")

    def parse(self, record):
        if record is None:
            return None
        return self.router(record)

    def parse_multiline(self, record) -> str:
        parsed_record = []
        for r in record:
            if r["type"] == "text":
                parsed_record.append(r["text"])
            else:
                raise ValueError(f"Invalid record type: {r['type']}, {r}")

        return "".join(parsed_record)

    def parse_number(self, record) -> float:
        return float(record)

    def parse_checkbox(self, record) -> bool:
        return record

    def parse_single_option(self, record) -> str:
        return record

    def parse_multiple_option(self, record) -> str:
        return ";".join(record)

    def parse_link(self, record) -> str:
        return record["link"]

    def parse_oneway_link(self, record) -> str:
        links = []
        table_id = self.field.property.table_id
        link_record_ids = (
            record["link_record_ids"] if "link_record_ids" in record else []
        )
        for link_record_id in link_record_ids:
            links.append(f"{table_id}:{link_record_id}")
        return ";".join(links)

    def parse_twoway_link(self, record) -> str:
        links = []
        table_id = self.field.property.table_id
        link_record_ids = (
            record["link_record_ids"] if "link_record_ids" in record else []
        )
        for link_record_id in link_record_ids:
            links.append(f"{table_id}:{link_record_id}")
        return ";".join(links)

    def parse_date(self, record) -> str:
        format = self.field.property.date_formatter
        format = format.replace("yyyy", "%Y")
        format = format.replace("MM", "%m")
        format = format.replace("dd", "%d")
        format = format.replace("HH", "%H")
        format = format.replace("mm", "%M")
        dt = datetime.fromtimestamp(record / 1000)
        return dt.strftime(format)

    def parse_progress(self, record) -> float:
        return float(record)
