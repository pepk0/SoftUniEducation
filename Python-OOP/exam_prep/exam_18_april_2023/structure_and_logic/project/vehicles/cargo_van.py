from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    cargo_van_max_mileage = 180.0

    def __init__(self, brand: str, model: str,
                 license_plate_number: str) -> None:
        super().__init__(brand, model, license_plate_number,
                         self.cargo_van_max_mileage)

    def drive(self, mileage: float) -> None:
        percent_reduction = round(
            (mileage / self.cargo_van_max_mileage) * 100) + 5
        self.battery_level -= percent_reduction
