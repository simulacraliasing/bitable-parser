from .resource import *

class V2:
    activity: Activity
    additional_information: AdditionalInformation
    additional_informations_batch: AdditionalInformationsBatch
    indicator: Indicator
    metric_detail: MetricDetail
    metric_field: MetricField
    metric_lib: MetricLib
    metric_tag: MetricTag
    metric_template: MetricTemplate
    question: Question
    review_data: ReviewData
    review_template: ReviewTemplate
    reviewee: Reviewee
    stage_task: StageTask
    user_group_user_rel: UserGroupUserRel
    def __init__(self, config: Config) -> None: ...
