from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    passenger_car_max_mileage = 450.0

    def __init__(self, brand: str, model: str,
                 license_plate_number: str) -> None:
        super().__init__(brand, model, license_plate_number,
                         self.passenger_car_max_mileage)

    def drive(self, mileage: float) -> None:
        percent_reduction = round(
            (mileage / self.passenger_car_max_mileage) * 100)
        self.battery_level -= percent_reduction
