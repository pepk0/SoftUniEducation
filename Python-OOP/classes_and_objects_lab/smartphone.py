class Smartphone:
    def __init__(self, memory: int) -> None:
        self.memory = memory
        self.apps: list = []
        self.is_on: bool = False

    def power(self) -> None:
        self.is_on = False if self.is_on else True

    def install(self, app: str, app_memory: int) -> str:
        if self.memory >= app_memory and self.is_on:
            self.memory -= app_memory
            self.apps.append(app)
            return f"Installing {app}"

        elif self.memory >= app_memory and not self.is_on:
            return f"Turn on your phone to install {app}"

        else:
            return f"Not enough memory to install {app}"

    def status(self) -> str:
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

# smartphone = Smartphone(100)
# print(smartphone.install("Facebook", 60))
# smartphone.power()
# print(smartphone.install("Facebook", 60))
# print(smartphone.install("Messenger", 20))
# print(smartphone.install("Instagram", 40))
# print(smartphone.status())
