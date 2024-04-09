from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int,
                 worker_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals: list = []
        self.workers: list = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget < price:
            return "Not enough budget"
        elif self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"

        self.__budget -= price
        self.animals.append(animal)
        return (f"{animal.name} the {animal.__class__.__name__} "
                f"added to the zoo")

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return (f"{worker.name} the {worker.__class__.__name__} "
                f"hired successfully")

    def fire_worker(self, worker_name: str) -> str:
        if worker_name in self.workers:
            self.workers.remove(worker_name)
            return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        amount_to_pay = sum(worker.salary for worker in self.workers)

        if self.__budget >= amount_to_pay:
            self.__budget -= amount_to_pay
            return (f"You payed your workers. They are happy. "
                    f"Budget left: {self.__budget}")

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        amount_for_tending = sum(
            animal.money_for_care for animal in self.animals)

        if self.__budget >= amount_for_tending:
            self.__budget -= amount_for_tending
            return (f"You tended all the animals. They are happy. "
                    f"Budget left: {self.__budget}")

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        type_animals = {"Lions": [], "Tigers": [], "Cheetahs": []}

        for animal in self.animals:
            type_animals[animal.__class__.__name__ + "s"].append(animal)

        all_animals = ""
        for animal_type, total_animals in type_animals.items():
            animals_string = '\n'.join(str(animal) for animal in total_animals)
            all_animals += (f"\n----- {len(total_animals)} {animal_type}:\n"
                            f"{animals_string}")

        return f"You have {len(self.animals)} animals{all_animals}"

    def workers_status(self) -> str:
        type_workers = {"Keepers": [], "Caretakers": [], "Vets": []}

        for worker in self.workers:
            type_workers[worker.__class__.__name__ + "s"].append(worker)

        all_workers = ""
        for worker_type, total_workers in type_workers.items():
            workers_string = '\n'.join(str(worker) for worker in total_workers)
            all_workers += (f"\n----- {len(total_workers)} {worker_type}:\n"
                            f"{workers_string}")

        return f"You have {len(self.workers)} workers{all_workers}"
