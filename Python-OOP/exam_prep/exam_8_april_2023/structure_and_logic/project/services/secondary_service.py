from project.services.base_service import BaseService


class SecondaryService(BaseService):
    type_ = "SecondaryService"
    second_service_capacity = 15

    def __init__(self, name: str) -> None:
        super().__init__(name, self.second_service_capacity)

    def details(self) -> str:
        robots = " ".join(
            x.name for x in self.robots) if self.robots else "none"
        return f"{self.name} Secondary Service:\nRobots: {robots}"
