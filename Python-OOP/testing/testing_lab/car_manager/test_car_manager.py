import unittest


# from car_manager import Car


class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car(
            "BMW",
            "320d",
            10,
            100,
        )

    def test_simple_init(self):
        self.assertEqual(self.car.make, "BMW")
        self.assertEqual(self.car.model, "320d")
        self.assertEqual(self.car.fuel_consumption, 10)
        self.assertEqual(self.car.fuel_capacity, 100)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_empty_car_make_should_give_error(self):
        with self.assertRaises(Exception) as empty_make:
            self.car.make = ""
        self.assertEqual(str(empty_make.exception),
                         "Make cannot be null or empty!")

    def test_empty_car_model_should_give_error(self):
        with self.assertRaises(Exception) as empty_make:
            self.car.model = ""
        self.assertEqual(str(empty_make.exception),
                         "Model cannot be null or empty!")

    def test_fuel_consumption_with_zero_or_negative_should_give_error(self):
        with self.assertRaises(Exception) as zero_fuel:
            self.car.fuel_consumption = 0

        with self.assertRaises(Exception) as negative_fuel:
            self.car.fuel_consumption = -10

        self.assertEqual(str(zero_fuel.exception),
                         "Fuel consumption cannot be zero or negative!")
        self.assertEqual(str(negative_fuel.exception),
                         "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_with_zero_or_negative_should_give_error(self):
        with self.assertRaises(Exception) as zero_fuel:
            self.car.fuel_capacity = 0

        with self.assertRaises(Exception) as negative_fuel:
            self.car.fuel_capacity = -10

        self.assertEqual(str(zero_fuel.exception),
                         "Fuel capacity cannot be zero or negative!")
        self.assertEqual(str(negative_fuel.exception),
                         "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_with_zero_gives_error(self):
        with self.assertRaises(Exception) as zero_amount:
            self.car.fuel_amount = -1

        self.assertEqual(str(zero_amount.exception),
                         "Fuel amount cannot be negative!")

    def test_refuel_method_gives_error_for_negative_or_zero(self):
        with self.assertRaises(Exception) as zero_fuel:
            self.car.refuel(0)

        with self.assertRaises(Exception) as negative_fuel:
            self.car.refuel(-1)

        self.assertEqual(str(zero_fuel.exception),
                         "Fuel amount cannot be zero or negative!")
        self.assertEqual(str(negative_fuel.exception),
                         "Fuel amount cannot be zero or negative!")

    def test_refuel_method_with_valid_and_more_then_capacity_value(self):
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_amount, 50)
        self.car.refuel(1000)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_method_with_more_distance_and_correct_distance(self):
        self.car.fuel_amount = 50
        with self.assertRaises(Exception) as fuel_exception:
            self.car.drive(1000)

        to_drive = 200
        prev_fuel = self.car.fuel_amount
        self.car.drive(to_drive)
        needed_fuel = (to_drive / 100) * self.car.fuel_consumption

        self.assertEqual(prev_fuel - needed_fuel, self.car.fuel_amount)
        self.assertEqual(str(fuel_exception.exception),
                         "You don't have enough fuel to drive!")


if __name__ == "__main__":
    unittest.main()
