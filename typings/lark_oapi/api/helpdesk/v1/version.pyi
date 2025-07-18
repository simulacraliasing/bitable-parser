from .resource import *

class V1:
    agent: Agent
    agent_schedules: AgentSchedules
    agent_schedule: AgentSchedule
    agent_skill: AgentSkill
    agent_skill_rule: AgentSkillRule
    bot_message: BotMessage
    category: Category
    event: Event
    faq: Faq
    notification: Notification
    ticket: Ticket
    ticket_message: TicketMessage
    ticket_customized_field: TicketCustomizedField
    def __init__(self, config: Config) -> None: ...
