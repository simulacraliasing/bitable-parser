import lark_oapi as lark
import pandas as pd
from lark_oapi.api.bitable.v1 import *

from bitable_parser.parser import RecordParser


class Table:
    def __init__(self, api_id, api_secret, app_token, table_id):
        self.client = (
            lark.Client()
            .builder()
            .app_id(api_id)
            .app_secret(api_secret)
            .log_level(lark.LogLevel.DEBUG)
            .build()
        )
        self.app_token = app_token
        self.table_id = table_id

    def fetch(self):
        records = {
            "record_id": {
                "data": [],
            },
        }
        fields = self.list_fields()
        for field in fields:
            records[field.field_name] = {
                "data": [],
                "parser": None,
            }
        has_more = True
        page_token = None
        while has_more:
            data = self.search_records(page_token)
            for item in data.items:
                d = item.fields
                records["record_id"]["data"].append(item.record_id)
                for field in fields:
                    records[field.field_name]["data"].append(
                        d.get(field.field_name, None)
                    )
            page_token = data.page_token
            has_more = data.has_more
        return records

    def list_fields(self):
        from lark_oapi.api.bitable.v1 import (
            ListAppTableFieldRequest,
            ListAppTableFieldResponse,
        )

        fields = []
        request = (
            ListAppTableFieldRequest.builder()
            .app_token(self.app_token)
            .table_id(self.table_id)
            .build()
        )

        response: ListAppTableFieldResponse = (
            self.client.bitable.v1.app_table_field.list(request)
        )

        if not response.success():
            raise ValueError(f"Error fetching data: {response.msg}, {response.error}")

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
        for field in response.data.items:
            if field.type not in field_type_map.keys():
                raise ValueError(f"Invalid field type: {field.type}")
            if field_type_map[field.type] not in valid_types:
                raise ValueError(f"Invalid field type: {field_type_map[field.type]}")
            fields.append(field)
        return fields

    def search_records(self, page_token=None):
        from lark_oapi.api.bitable.v1 import (
            SearchAppTableRecordRequest,
            SearchAppTableRecordRequestBody,
            SearchAppTableRecordResponse,
        )

        request = (
            SearchAppTableRecordRequest.builder()
            .app_token(self.app_token)
            .table_id(self.table_id)
            .page_size(500)
            .request_body(SearchAppTableRecordRequestBody.builder().build())
        )
        if page_token:
            request = request.page_token(page_token).build()
        else:
            request = request.build()
        response: SearchAppTableRecordResponse = (
            self.client.bitable.v1.app_table_record.search(request)
        )
        if not response.success():
            raise ValueError(f"Error fetching data: {response.msg}, {response.error}")
        return response.data

    def to_dataframe(self):
        records = self.fetch()
        for field in self.list_fields():
            records[field.field_name]["parser"] = RecordParser(field)
        parsed_records = {}
        for key, value in records.items():
            if key == "record_id":
                parsed_records[key] = value["data"]
                continue
            parser = value["parser"]
            parsed_data = []
            for d in value["data"]:
                parsed_data.append(parser.parse(d))
            parsed_records[key] = parsed_data
        return pd.DataFrame(parsed_records)

    def update_record(self, record_id, data):
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
        response: UpdateAppTableRecordResponse = (
            self.client.bitable.v1.app_table_record.update(request)
        )

        if not response.success():
            raise ValueError(f"Error updating record: {response.msg}, {response.error}")

    def update_batch_records(self, data):
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
                    AppTableRecord.builder()
                    .fields(record["fields"])
                    .record_id(record["record_id"])
                    .build()
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

        response: BatchUpdateAppTableRecordResponse = (
            self.client.bitable.v1.app_table_record.batch_update(request)
        )

        if not response.success():
            raise ValueError(f"Error updating record: {response.msg}, {response.error}")
