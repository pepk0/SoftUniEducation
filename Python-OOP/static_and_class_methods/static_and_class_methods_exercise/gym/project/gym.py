from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self) -> None:
        self.customers: list = []
        self.trainers: list = []
        self.equipment: list = []
        self.plans: list = []
        self.subscriptions: list = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def subscription_info(self, subscription_id: int) -> str:
        if subscription_id in self.subscriptions:
            subscription = self.subscriptions[
                self.subscriptions.index(subscription_id)]
            customer = self.customers[
                self.customers.index(subscription.customer_id)]
            trainer = self.trainers[
                self.trainers.index(subscription.trainer_id)]
            exercise = self.plans[self.plans.index(subscription.exercise_id)]
            equipment = self.equipment[
                self.equipment.index(exercise.equipment_id)]

            return (f"{subscription}\n{customer}\n{trainer}\n{equipment}"
                    f"\n{exercise}")
