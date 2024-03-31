from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    type_ = "FemaleRobot"
    possible_service = "SecondaryService"
    female_robot_initial_weight = 7

    def __init__(self, name: str, kind: str, price: float) -> None:
        super().__init__(name, kind, price, self.female_robot_initial_weight)

    def eating(self) -> None:
        self.weight += 1
