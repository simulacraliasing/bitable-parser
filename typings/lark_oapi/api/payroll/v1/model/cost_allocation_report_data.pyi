from .compensation_cost_item import CompensationCostItem as CompensationCostItem
from .data_summary_dimension import DataSummaryDimension as DataSummaryDimension
from lark_oapi.core.construct import init as init

class CostAllocationReportData:
    data_summary_dimensions: list[DataSummaryDimension] | None
    compensation_cost_item: CompensationCostItem | None
    employment_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CostAllocationReportDataBuilder: ...

class CostAllocationReportDataBuilder:
    def __init__(self) -> None: ...
    def data_summary_dimensions(self, data_summary_dimensions: list[DataSummaryDimension]) -> CostAllocationReportDataBuilder: ...
    def compensation_cost_item(self, compensation_cost_item: CompensationCostItem) -> CostAllocationReportDataBuilder: ...
    def employment_id(self, employment_id: str) -> CostAllocationReportDataBuilder: ...
    def build(self) -> CostAllocationReportData: ...
