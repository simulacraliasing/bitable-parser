from .resource import *

class V1:
    bank_card: BankCard
    business_card: BusinessCard
    business_license: BusinessLicense
    chinese_passport: ChinesePassport
    contract: Contract
    driving_license: DrivingLicense
    food_manage_license: FoodManageLicense
    food_produce_license: FoodProduceLicense
    health_certificate: HealthCertificate
    hkm_mainland_travel_permit: HkmMainlandTravelPermit
    id_card: IdCard
    resume: Resume
    taxi_invoice: TaxiInvoice
    train_invoice: TrainInvoice
    tw_mainland_travel_permit: TwMainlandTravelPermit
    vat_invoice: VatInvoice
    vehicle_invoice: VehicleInvoice
    vehicle_license: VehicleLicense
    def __init__(self, config: Config) -> None: ...
