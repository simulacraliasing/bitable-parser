from .category import Category as Category
from .richtext import Richtext as Richtext
from .ticket_user import TicketUser as TicketUser
from lark_oapi.core.construct import init as init

class Faq:
    faq_id: str | None
    id: str | None
    helpdesk_id: str | None
    question: str | None
    answer: str | None
    answer_richtext: list[Richtext] | None
    create_time: int | None
    update_time: int | None
    categories: list[Category] | None
    tags: list[str] | None
    expire_time: int | None
    update_user: TicketUser | None
    create_user: TicketUser | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> FaqBuilder: ...

class FaqBuilder:
    def __init__(self) -> None: ...
    def faq_id(self, faq_id: str) -> FaqBuilder: ...
    def id(self, id: str) -> FaqBuilder: ...
    def helpdesk_id(self, helpdesk_id: str) -> FaqBuilder: ...
    def question(self, question: str) -> FaqBuilder: ...
    def answer(self, answer: str) -> FaqBuilder: ...
    def answer_richtext(self, answer_richtext: list[Richtext]) -> FaqBuilder: ...
    def create_time(self, create_time: int) -> FaqBuilder: ...
    def update_time(self, update_time: int) -> FaqBuilder: ...
    def categories(self, categories: list[Category]) -> FaqBuilder: ...
    def tags(self, tags: list[str]) -> FaqBuilder: ...
    def expire_time(self, expire_time: int) -> FaqBuilder: ...
    def update_user(self, update_user: TicketUser) -> FaqBuilder: ...
    def create_user(self, create_user: TicketUser) -> FaqBuilder: ...
    def build(self) -> Faq: ...
