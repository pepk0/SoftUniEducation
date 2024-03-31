from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {"MainService": MainService,
                      "SecondaryService": SecondaryService}
    VALID_ROBOTS_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self) -> None:
        self.robots: list = []
        self.services: list = []

    @staticmethod
    def get_item_by_name(name: str, collection):
        return [r for r in collection if r.name == name][0]

    def add_service(self, service_type: str, name: str) -> str:
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICES[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str,
                  price: float) -> str:
        if robot_type not in self.VALID_ROBOTS_TYPES:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOTS_TYPES[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = self.get_item_by_name(robot_name, self.robots)
        service = self.get_item_by_name(service_name, self.services)

        if robot.possible_service != service.type_:
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str,
                                  service_name: str) -> str:

        service = self.get_item_by_name(service_name, self.services)
        try:
            robot = self.get_item_by_name(robot_name, service.robots)
        except IndexError:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = self.get_item_by_name(service_name, self.services)

        robots_feed = 0
        for robot in service.robots:
            robot.eating()
            robots_feed += 1

        return f"Robots fed: {robots_feed}."

    def service_price(self, service_name: str) -> str:
        service = self.get_item_by_name(service_name, self.services)

        price = sum(x.price for x in service.robots)
        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self) -> str:
        return "\n".join(service.details() for service in self.services)
