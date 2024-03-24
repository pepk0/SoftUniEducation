import unittest


# from worker import Worker


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Peter", 100, 100)

    def test_worker_initialization(self):
        self.assertEqual(self.worker.name, "Peter")
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_rest_method_increments_correctly(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 101)

    def test_work_method_with_negative_value_or_zero_value(self):
        self.worker.energy = -12
        with self.assertRaises(Exception) as negative:
            self.worker.work()

        self.worker.energy = 0
        with self.assertRaises(Exception) as zero:
            self.worker.work()

        self.assertEqual(str(negative.exception), "Not enough energy.")
        self.assertEqual(str(zero.exception), "Not enough energy.")

    def test_work_method_gives_correct_money(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 100)

    def test_work_method_decreases_energy(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 99)

    def test_get_info_method(self):
        info = "Peter has saved 0 money."
        self.assertEqual(self.worker.get_info(), info)


if __name__ == "__main__":
    unittest.main()
