#!/usr/bin/bash
"""
Author: Ian
Purpose: 
Input:
Output:

"""

import unittest

from L22_genparenth import generatePa


class TestGenPa(unittest.TestCase):
    def test_gen_pa(self):
        """
        Test that it can sum a list of integers
        """
        data = 2
        result = generatePa(data)
        self.assertEqual(result, ['(())', '()()'])

if __name__ == '__main__':
    unittest.main()