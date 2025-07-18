from typing import Any

import lark_oapi as lark
import pandas as pd
from lark_oapi.api.bitable.v1 import *
from lark_oapi.core.enum import LogLevel

from .parser import RecordParser, parse_filter


class Table:
    def __init__(
        self, api_id: str, api_secret: str, app_token: str, table_id: str, log_level: LogLevel = LogLevel.INFO
    ):
        self.client: lark.client.Client = (
            lark.client.Client().builder().app_id(api_id).app_secret(api_secret).log_level(log_level).build()
        )
        self.app_token = app_token
        self.table_id = table_id

    def fetch(self, field_names: list[str] | None = None, filter: str | None = None, page_size: int = 500):
        records: dict[str, dict[str, Any]] = {
            "record_id": {
                "data": [],
            },
        }
        fields = self.list_fields()
        if field_names:
            fields = [field for field in fields if field.field_name in field_names]
        for field in fields:
            if field.field_name is None:
                continue
            records[field.field_name] = {
                "data": [],
                "parser": None,
            }
        has_more = True
        page_token = None
        while has_more:
            data = self.search_records(page_token, field_names=field_names, filter=filter, page_size=page_size)
            if data is None or data.items is None:
                return records, fields
            for item in data.items:
                d = item.fields
                if d is None:
                    continue
                records["record_id"]["data"].append(item.record_id)
                for field in fields:
                    if field.field_name is None:
                        continue
                    records[field.field_name]["data"].append(d.get(field.field_name, None))
            page_token = data.page_token
            has_more = data.has_more
        return records, fields

    def list_fields(self):
        from lark_oapi.api.bitable.v1 import AppTableFieldForList, ListAppTableFieldRequest

        fields: list[AppTableFieldForList] = []
        request = ListAppTableFieldRequest.builder().app_token(self.app_token).table_id(self.table_id).build()

        bitable_service = self.client.bitable

        if not bitable_service:
            raise ValueError()

        response = bitable_service.v1.app_table_field.list(request)

        if not response.success():
            raise ValueError(f"Error list fields: {response.msg}, {response.error}")

        field_type_map = {
            1: "multiline",
            2: "number",
            3: "single_option",
            4: "multiple_options",
            5: "date",
            7: "checkbox",
            11: "person",
            13: "phone_number",
            15: "link",
            17: "attachment",
            18: "oneway_link",
            20: "formula",
            21: "twoway_link",
            22: "location",
            23: "groupchat",
            1001: "create_time",
            1002: "update_time",
            1003: "create_by",
            1004: "update_by",
        }
        valid_types = [
            "multiline",
            "number",
            "single_option",
            "multiple_options",
            "date",
            "link",
            "checkbox",
            "oneway_link",
            "twoway_link",
        ]
        if not response.data:
            raise ValueError(f"Table {self.table_id} is empty")
        if not response.data.items:
            raise ValueError(f"Table {self.table_id} is empty")
        for field in response.data.items:
            if not field.type:
                raise ValueError(f"Field {field.field_name} has no type")
            if field.type not in field_type_map.keys():
                raise ValueError(f"Invalid field type: {field.type}")
            if field_type_map[field.type] not in valid_types:
                raise ValueError(f"Invalid field type: {field_type_map[field.type]}")
            fields.append(field)
        return fields

    def search_records(
        self,
        page_token: str | None = None,
        field_names: list[str] | None = None,
        filter: str | None = None,
        page_size: int = 500,
    ):
        from lark_oapi.api.bitable.v1 import (
            SearchAppTableRecordRequest,
            SearchAppTableRecordRequestBody,
            SearchAppTableRecordResponse,
        )

        request_body = SearchAppTableRecordRequestBody.builder()
        if field_names:
            request_body = request_body.field_names(field_names)
        if filter:
            request_body = request_body.filter(parse_filter(filter))
        request_body = request_body.automatic_fields(False).build()
        request = (
            SearchAppTableRecordRequest.builder()
            .app_token(self.app_token)
            .table_id(self.table_id)
            .page_size(page_size)
            .request_body(request_body)
        )
        if page_token:
            request = request.page_token(page_token).build()
        else:
            request = request.build()
        if not self.client.bitable:
            raise ValueError("Empty bitable")
        response: SearchAppTableRecordResponse = self.client.bitable.v1.app_table_record.search(request)
        if not response.success():
            raise ValueError(f"Error fetching data: {response.msg}, {response.error}")
        return response.data

    def to_dataframe(self, field_names: list[str] | None = None, filter: str | None = None, page_size: int = 500):
        records, fields = self.fetch(field_names=field_names, filter=filter, page_size=page_size)
        for field in fields:
            if field.field_name is None:
                continue
            records[field.field_name]["parser"] = RecordParser(field)
        parsed_records = {}
        for key, value in records.items():
            if key == "record_id":
                parsed_records[key] = value["data"]
                continue
            parser: RecordParser = value["parser"]
            parsed_data: list[Any] = []
            for d in value["data"]:
                parsed_data.append(parser.parse(d))
            parsed_records[key] = parsed_data
        return pd.DataFrame(parsed_records)

    def update_record(self, record_id: str, data: dict[str, Any]):
        from lark_oapi.api.bitable.v1 import (
            AppTableRecord,
            UpdateAppTableRecordRequest,
            UpdateAppTableRecordResponse,
        )

        request = (
            UpdateAppTableRecordRequest.builder()
            .app_token(self.app_token)
            .table_id(self.table_id)
            .record_id(record_id)
            .request_body(AppTableRecord.builder().fields(data).build())
            .build()
        )
        if not self.client.bitable:
            raise ValueError("Biable not available")
        response: UpdateAppTableRecordResponse = self.client.bitable.v1.app_table_record.update(request)

        if not response.success():
            raise ValueError(f"Error updating record: {response.msg}, {response.error}")

    def update_batch_records(self, data: list[dict[str, Any]]):
        from lark_oapi.api.bitable.v1 import (
            AppTableRecord,
            BatchUpdateAppTableRecordRequest,
            BatchUpdateAppTableRecordRequestBody,
            BatchUpdateAppTableRecordResponse,
        )

        if len(data) > 1000:
            raise ValueError(f"Record size: {len(data)} exceeds the limit of 1000")

        request_body = (
            BatchUpdateAppTableRecordRequestBody.builder()
            .records(
                [
                    AppTableRecord.builder().fields(record["fields"]).record_id(record["record_id"]).build()
                    for record in data
                ]
            )
            .build()
        )

        request = (
            BatchUpdateAppTableRecordRequest.builder()
            .app_token(self.app_token)
            .table_id(self.table_id)
            .request_body(request_body)
            .build()
        )
        if not self.client.bitable:
            raise ValueError("Biable not available")
        response: BatchUpdateAppTableRecordResponse = self.client.bitable.v1.app_table_record.batch_update(request)

        if not response.success():
            raise ValueError(f"Error updating record: {response.msg}, {response.error}")
