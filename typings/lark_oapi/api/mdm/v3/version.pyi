from .resource import *

class V3:
    batch_country_region: BatchCountryRegion
    country_region: CountryRegion
    def __init__(self, config: Config) -> None: ...
