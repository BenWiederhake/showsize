#!/usr/bin/env python3

import showsize
import unittest


TEST_BATTERY = [
    (1024.0, "1.0 KiB"),
    (2048.0, "2.0 KiB"),
    (1048576.0, "1.0 MiB"),
]


class StringConversion(unittest.TestCase):
    def test_basic(self):
        for size_bytes, expected_size_human in TEST_BATTERY:
            with self.subTest(size_bytes=size_bytes, expected_size_human=expected_size_human):
                actual_size_human = showsize.human_readable(size_bytes)
                self.assertEqual(expected_size_human, actual_size_human)


if __name__ == "__main__":
    unittest.main()
