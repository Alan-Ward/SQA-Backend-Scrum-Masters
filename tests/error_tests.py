import unittest
from unittest.mock import patch
import io
from src.print_error import log_constraint_error

class TestPrintError(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_log_constraint_error(self, mock_stdout):
        log_constraint_error("Invalid code", "Status")
        self.assertEqual(mock_stdout.getvalue(), "ERROR: Status: Invalid code\n")

if __name__ == '__main__':
    unittest.main()