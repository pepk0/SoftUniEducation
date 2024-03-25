import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100.5, 150.3)

    def test_innit_method(self):
        self.assertEqual(self.vehicle.fuel, 100.5)
        self.assertEqual(self.vehicle.capacity, 100.5)
        self.assertEqual(self.vehicle.horse_power, 150.3)
        self.assertEqual(self.vehicle.fuel_consumption,
                         Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_method_gives_error_for_not_enough_fuel(self):
        with self.assertRaises(Exception) as fuel_exception:
            self.vehicle.drive(200)

        self.assertEqual(str(fuel_exception.exception), "Not enough fuel")

    def test_drive_method_with_correct_kilometers(self):
        expected = self.vehicle.fuel - 50 * Vehicle.DEFAULT_FUEL_CONSUMPTION
        self.vehicle.drive(50)
        self.assertEqual(self.vehicle.fuel, expected)

    def test_refuel_method_with_more_fuel(self):
        with self.assertRaises(Exception) as fuel_exception:
            self.vehicle.refuel(1000)

        self.assertEqual(str(fuel_exception.exception), "Too much fuel")

    def test_refuel_with_correct_argument(self):
        self.vehicle.fuel = 0
        expected = self.vehicle.fuel + 20
        self.vehicle.refuel(20)
        self.assertEqual(expected, self.vehicle.fuel)

    def test_class_str_method(self):
        expected = (f"The vehicle has 150.3 horse power with 100.5 fuel left "
                    f"and {Vehicle.DEFAULT_FUEL_CONSUMPTION} fuel consumption")

        self.assertEqual(str(self.vehicle), expected)


if __name__ == '__main__':
    unittest.main()
