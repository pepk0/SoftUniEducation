from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: list = []
        self.dvds: list = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def get_customer_and_dvd(self, customer_id: int, dvd_id: int) -> tuple:
        customer = None
        dvd = None
        if dvd_id in self.dvds:
            dvd = self.dvds[self.dvds.index(dvd_id)]
        if customer_id in self.customers:
            customer = self.customers[self.customers.index(customer_id)]
        return customer, dvd

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str or None:
        customer, dvd = self.get_customer_and_dvd(customer_id, dvd_id)
        if customer and dvd:

            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            elif dvd.is_rented:
                return "DVD is already rented"
            elif customer.age < dvd.age_restriction:
                return (f"{customer.name} should be at least "
                        f"{dvd.age_restriction} to rent this movie")

            customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str or None:
        customer, dvd = self.get_customer_and_dvd(customer_id, dvd_id)
        if customer and dvd:
            if dvd in customer.rented_dvds:
                customer.rented_dvds.remove(dvd)
                dvd.is_rented = False
                return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self) -> str:
        return "\n".join([str(person) for person in self.customers]
                         + [str(dvd) for dvd in self.dvds])
