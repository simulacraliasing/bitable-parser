from .website_delivery_customized_data import WebsiteDeliveryCustomizedData as WebsiteDeliveryCustomizedData
from lark_oapi.core.construct import init as init

class WebsiteDeliveryAward:
    customized_data: list[WebsiteDeliveryCustomizedData] | None
    desc: str | None
    title: str | None
    award_time: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> WebsiteDeliveryAwardBuilder: ...

class WebsiteDeliveryAwardBuilder:
    def __init__(self) -> None: ...
    def customized_data(self, customized_data: list[WebsiteDeliveryCustomizedData]) -> WebsiteDeliveryAwardBuilder: ...
    def desc(self, desc: str) -> WebsiteDeliveryAwardBuilder: ...
    def title(self, title: str) -> WebsiteDeliveryAwardBuilder: ...
    def award_time(self, award_time: int) -> WebsiteDeliveryAwardBuilder: ...
    def build(self) -> WebsiteDeliveryAward: ...
