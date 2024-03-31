from project.services.base_service import BaseService


class MainService(BaseService):
    type_ = "MainService"
    main_service_capacity = 30

    def __init__(self, name: str) -> None:
        super().__init__(name, self.main_service_capacity)

    def details(self) -> str:
        robots = " ".join(
            x.name for x in self.robots) if self.robots else "none"
        return f"{self.name} Main Service:\nRobots: {robots}"
