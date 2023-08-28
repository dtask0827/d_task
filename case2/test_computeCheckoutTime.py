from queue import computeCheckoutTime_1, computeCheckoutTime_2
import unittest


def test_functions(func):
    class TestComputeCheckoutTime_x(unittest.TestCase):
        def test_computeCheckoutTime_x(self):
            self.assertEqual(func([5, 3, 4], 1), 12)
            self.assertEqual(func([10, 2, 3, 3], 2), 10)
            self.assertEqual(func([2, 3, 10], 2), 12)
            self.assertEqual(
                func([27, 10, 2, 2, 10, 39, 38, 45, 7, 19, 5, 42, 7, 5, 49], 4), 104)
            self.assertEqual(
                func([49, 49, 38, 33, 43, 9, 14, 12, 31, 42, 33, 49], 5), 101)
            self.assertEqual(func([], 1), 0)

    return TestComputeCheckoutTime_x


class TestComputeCheckoutTime_1(test_functions(computeCheckoutTime_1)):
    pass


class TestComputeCheckoutTime_2(test_functions(computeCheckoutTime_2)):
    pass


if __name__ == '__main__':
    unittest.main()
