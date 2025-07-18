from .resource import *

class V1:
    acct_item: AcctItem
    cost_allocation_plan: CostAllocationPlan
    cost_allocation_report: CostAllocationReport
    datasource: Datasource
    datasource_record: DatasourceRecord
    paygroup: Paygroup
    payment_activity: PaymentActivity
    payment_activity_detail: PaymentActivityDetail
    payment_detail: PaymentDetail
    def __init__(self, config: Config) -> None: ...
