from .vehicle_invoice import VehicleInvoice as VehicleInvoice
from lark_oapi.core.construct import init as init

class RecognizeVehicleInvoiceResponseBody:
    vehicle_invoice: VehicleInvoice | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RecognizeVehicleInvoiceResponseBodyBuilder: ...

class RecognizeVehicleInvoiceResponseBodyBuilder:
    def __init__(self) -> None: ...
    def vehicle_invoice(self, vehicle_invoice: VehicleInvoice) -> RecognizeVehicleInvoiceResponseBodyBuilder: ...
    def build(self) -> RecognizeVehicleInvoiceResponseBody: ...
