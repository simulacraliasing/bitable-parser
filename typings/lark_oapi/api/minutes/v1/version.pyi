from .resource import *

class V1:
    minute: Minute
    minute_media: MinuteMedia
    minute_statistics: MinuteStatistics
    minute_transcript: MinuteTranscript
    def __init__(self, config: Config) -> None: ...
