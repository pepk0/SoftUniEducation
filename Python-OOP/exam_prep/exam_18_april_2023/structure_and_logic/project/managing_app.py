from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    valid_vehicle_types = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self) -> None:
        self.users: list = []
        self.vehicles: list = []
        self.routes: list = []

    def get_user_by_license(self, number: str) -> User:
        return [u for u in self.users if u.driving_license_number == number][0]

    def get_car_by_plate(self, plate: str) -> BaseVehicle:
        return [c for c in self.vehicles if c.license_plate_number == plate][0]

    def get_route_by_id(self, _id: int) -> Route:
        return [r for r in self.routes if r.route_id == _id][0]

    def register_user(self, first_name: str, last_name: str,
                      driving_license_number: str) -> str:
        if driving_license_number in [user.driving_license_number for user in
                                      self.users]:
            return (f"{driving_license_number} has already "
                    f"been registered to our platform.")

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return (f"{first_name} {last_name} was successfully "
                f"registered under DLN-{driving_license_number}")

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str,
                       license_plate_number: str) -> str:
        if vehicle_type not in self.valid_vehicle_types:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if license_plate_number in [x.license_plate_number for x in
                                    self.vehicles]:
            return f"{license_plate_number} belongs to another vehicle."

        vehicle = self.valid_vehicle_types[vehicle_type](brand, model,
                                                         license_plate_number)
        self.vehicles.append(vehicle)
        return (f"{brand} {model} was successfully uploaded "
                f"with LPN-{license_plate_number}.")

    def allow_route(self, start_point: str, end_point: str,
                    length: float) -> str:
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return (f"{start_point}/{end_point} - {length} km had "
                            f"already been added to our platform.")
                elif route.length < length:
                    return (f"{start_point}/{end_point} shorter route had "
                            f"already been added to our platform.")
                elif route.length > length:
                    route.is_locked = True

        route_new_id = len(self.routes) + 1
        route = Route(start_point, end_point, length, route_new_id)
        self.routes.append(route)
        return (f"{start_point}/{end_point} - {length} km is unlocked "
                f"and available to use.")

    def make_trip(self, driving_license_number: str, license_plate_number: str,
                  route_id: int, is_accident_happened: bool) -> str:

        user = self.get_user_by_license(driving_license_number)
        vehicle = self.get_car_by_plate(license_plate_number)
        route = self.get_route_by_id(route_id)

        if user.is_blocked:
            return (f"User {driving_license_number} is blocked in the platform!"
                    f" This trip is not allowed.")

        if vehicle.is_damaged:
            return (f"Vehicle {license_plate_number} is damaged! "
                    f"This trip is not allowed.")

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int) -> str:
        damaged_vehicles = [x for x in self.vehicles if x.is_damaged]
        sorted_vehicles = sorted(damaged_vehicles,
                                 key=lambda c: (c.brand, c.model))
        repaired_vehicles = 0
        try:
            for index in range(count):
                sorted_vehicles[index].change_status()
                sorted_vehicles[index].recharge()
                repaired_vehicles += 1
        except IndexError:
            pass

        return f"{repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self) -> str:
        sorted_users = "\n".join(
            str(x) for x in sorted(self.users, key=lambda u: -u.rating))
        return f"*** E-Drive-Rent ***\n{sorted_users}"
