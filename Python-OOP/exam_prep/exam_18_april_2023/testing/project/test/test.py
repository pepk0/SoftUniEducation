from project.robot import Robot
import unittest


class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot_one = Robot("1", "Military", 10, 10.4)
        self.robot_two = Robot("2", "Military", 10, 20.4)
        self.robot_tree = Robot("3", "Military", 10, 5.4)
        self.robot_four = Robot("4", "Military", 10, 10.4)

    def test_simple_init(self):
        self.assertEqual(self.robot_one.robot_id, "1")
        self.assertEqual(self.robot_one.category, "Military")
        self.assertEqual(self.robot_one.available_capacity, 10)
        self.assertEqual(self.robot_one.price, 10.4)
        self.assertEqual(self.robot_one.hardware_upgrades, [])
        self.assertEqual(self.robot_one.software_updates, [])

    def test_category_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.robot_one.category = "not a real category"

        self.assertEqual(str(ex.exception),
                         f"Category should be one of "
                         f"'['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_price_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.robot_one.price = -20

        self.assertEqual(str(ex.exception), "Price cannot be negative!")

    def test_upgrade_with_existing_item(self):
        self.robot_one.hardware_upgrades.append("test")
        result = self.robot_one.upgrade("test", 1.2)

        self.assertEqual(result, f"Robot 1 was not upgraded.")

    def test_upgrade_with_valid_item(self):
        result = self.robot_one.upgrade("test", 2)

        self.assertIn("test", self.robot_one.hardware_upgrades)
        self.assertEqual(self.robot_one.price, 13.4)
        self.assertEqual(result, f'Robot 1 was upgraded with test.')
        self.assertEqual(self.robot_one.hardware_upgrades, ["test"])

    def test_update_with_invalid_result_for_capacity(self):
        result = self.robot_one.update(2, 12)
        self.assertEqual(result, "Robot 1 was not updated.")

    def test_update_with_invalid_result_for_version(self):
        self.robot_one.software_updates.append(3)
        result = self.robot_one.update(2, 5)
        self.assertEqual(result, "Robot 1 was not updated.")

    def test_update_with_valid_results(self):
        result = self.robot_one.update(1.2, 5)
        self.assertEqual(result, f'Robot 1 was updated to version 1.2.')
        self.assertEqual(self.robot_one.available_capacity, 5)
        self.assertEqual(self.robot_one.software_updates, [1.2])

    def test_dunder_gt_method_more_expensive(self):
        self.assertEqual(self.robot_one > self.robot_tree,
                         'Robot with ID 1 is more expensive'
                         ' than Robot with ID 3.')

    def test_dunder_gt_method_more_cheaper(self):
        self.assertEqual(self.robot_one > self.robot_two,
                         'Robot with ID 1 is cheaper than Robot with ID 2.')

    def test_dunder_gt_method_equal(self):
        self.assertEqual(self.robot_one > self.robot_four,
                         'Robot with ID 1 costs equal to Robot with ID 4.')


if __name__ == '__main__':
    unittest.main()
