from __future__ import division, print_function, unicode_literals

import unittest

from buyer import do_calculation

TEST_OFFER = [
    {
        "Quantity": 12.00000000,
        "Rate": 0.02525000
    },
    {
        "Quantity": 15.37000000,
        "Rate": 0.02515000
    },
    {
        "Quantity": 11.37000000,
        "Rate": 0.02505000
    },
]


class TestCalculation(unittest.TestCase):

    def test_example(self):
        total_get, amount_left = do_calculation(TEST_OFFER, 16)
        self.assertAlmostEqual(total_get, 0.4036)
        self.assertEqual(amount_left, 0)

    def test_too_many(self):
        total_get, amount_left = do_calculation(TEST_OFFER, 160)
        self.assertAlmostEqual(total_get, 0.974374)
        self.assertAlmostEqual(amount_left, 121.26)


if __name__ == '__main__':
    unittest.main()
