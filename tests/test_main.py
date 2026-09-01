import unittest
from src.main import main


class TestMain(unittest.TestCase):
    def test_main_exists(self):
        """Test that main function exists."""
        self.assertTrue(callable(main))


if __name__ == '__main__':
    unittest.main()