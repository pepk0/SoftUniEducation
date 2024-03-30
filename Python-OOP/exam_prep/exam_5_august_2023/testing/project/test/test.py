from project.second_hand_car import SecondHandCar
import unittest


class TestSecondHandCar(unittest.TestCase):
    def setUp(self):
        self.test_car_one = SecondHandCar("bmw", "sedan", 200, 20.3)
        self.test_car_two = SecondHandCar("VW", "combi", 243, 15.4)
        self.test_car_tree = SecondHandCar("honda", "sedan", 2330, 10.3)

    def test_simple_init(self):
        self.assertEqual(self.test_car_one.model, "bmw")
        self.assertEqual(self.test_car_one.car_type, "sedan")
        self.assertEqual(self.test_car_one.mileage, 200)
        self.assertEqual(self.test_car_one.price, 20.3)

    def test_price_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.test_car_one.price = 0

        self.assertEqual(str(ex.exception), 'Price should be greater than 1.0!')

    def test_mileage_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.test_car_one.mileage = 0

        self.assertEqual(str(ex.exception), 'Please, second-hand cars only! '
                                            'Mileage must be greater than 100!')

    def test_set_promotion_with_higher_price_then_normal_one(self):
        with self.assertRaises(ValueError) as ex:
            self.test_car_one.set_promotional_price(2000)

        self.assertEqual(str(ex.exception),
                         'You are supposed to decrease the price!')

    def test_set_promotion_with_valid_new_price(self):
        new_price = 1.5
        result = self.test_car_one.set_promotional_price(new_price)

        self.assertEqual(self.test_car_one.price, new_price)
        self.assertEqual(result,
                         'The promotional price has been successfully set.')

    def test_need_repair_with_impossible_repair(self):
        result = self.test_car_one.need_repair(20.5, "test")

        self.assertEqual(result, 'Repair is impossible!')

    def test_need_repair_with_possible_repair_price(self):
        result = self.test_car_one.need_repair(10, "repair")

        self.assertEqual(result,
                         'Price has been increased due to repair charges.')

    def test_need_repair_with_possible_repair_price_price_increase(self):
        new_price = self.test_car_one.price + 10
        self.test_car_one.need_repair(10, "repair")
        self.assertEqual(new_price, self.test_car_one.price)

    def test_need_repair_with_possible_repair_is_done(self):
        self.test_car_one.need_repair(10, "repair")
        self.assertEqual(len(self.test_car_one.repairs), 1)

    def test_gt_class_method_with_same_objects(self):
        self.assertTrue(self.test_car_one > self.test_car_tree)

    def test_gt_class_method_with_different_objects(self):
        result = self.test_car_one > self.test_car_two
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_str_method(self):
        result = f"""Model bmw | Type sedan | Milage 200km
Current price: 20.30 | Number of Repairs: 0"""

        self.assertEqual(result, str(self.test_car_one))


if __name__ == '__main__':
    unittest.main()
