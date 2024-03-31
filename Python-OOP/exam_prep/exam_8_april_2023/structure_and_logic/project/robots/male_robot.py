from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    type_ = "MaleRobot"
    possible_service = "MainService"
    male_robot_initial_weight = 9

    def __init__(self, name: str, kind: str, price: float) -> None:
        super().__init__(name, kind, price, self.male_robot_initial_weight)

    def eating(self) -> None:
        self.weight += 3
