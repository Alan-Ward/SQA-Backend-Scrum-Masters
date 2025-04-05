import unittest
import os
import tempfile

from src.readTransaction import read_transaction_file

class TestTransactionFileReader(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        # Clean up temporary files
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def test_valid_transaction_line(self):
        """Test a correctly formatted transaction line."""
        test_file = os.path.join(self.test_dir, "valid.txt")
        with open(test_file, 'w') as f:
            f.write("12 John Doe             12345 00100.00\n")  # 38 chars
        
        transactions = read_transaction_file(test_file)
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]['transaction_code'], '12')
        self.assertEqual(transactions[0]['name'], 'John Doe             ')
        self.assertEqual(transactions[0]['account_number'], '12345')
        self.assertEqual(transactions[0]['transaction_amount'], 100.00)

    def test_invalid_line_length(self):
        """Test a line with incorrect length."""
        test_file = os.path.join(self.test_dir, "invalid_length.txt")
        with open(test_file, 'w') as f:
            f.write("12 ShortLine 123 1.00\n")  # Too short
        
        transactions = read_transaction_file(test_file)
        self.assertEqual(len(transactions), 0)  # Should skip invalid line

    def test_invalid_transaction_code(self):
        """Test a line with a non-digit transaction code."""
        test_file = os.path.join(self.test_dir, "invalid_code.txt")
        with open(test_file, 'w') as f:
            f.write("AB John Doe             12345 00100.00\n")  # 'AB' instead of digits
        
        transactions = read_transaction_file(test_file)
        self.assertEqual(len(transactions), 0)  # Should skip invalid line

    def test_invalid_transaction_amount(self):
        """Test a line with malformed transaction amount."""
        test_file = os.path.join(self.test_dir, "invalid_amount.txt")
        with open(test_file, 'w') as f:
            f.write("12 John Doe             12345 100XX.00\n")  # Invalid digits
        
        transactions = read_transaction_file(test_file)
        self.assertEqual(len(transactions), 0)  # Should skip invalid line

    def test_invalid_account_number(self):
        """Test a line with non-digit account number."""
        test_file = os.path.join(self.test_dir, "invalid_account.txt")
        with open(test_file, 'w') as f:
            f.write("12 John Doe             ABCDE 00100.00\n")  # Letters in account number
        
        transactions = read_transaction_file(test_file)
        self.assertEqual(len(transactions), 0)  # Should skip invalid line

    def test_empty_file(self):
        """Test an empty file."""
        test_file = os.path.join(self.test_dir, "empty.txt")
        with open(test_file, 'w') as f:
            pass  # Empty file
        
        transactions = read_transaction_file(test_file)
        self.assertEqual(len(transactions), 0)

    def test_file_not_found(self):
        """Test handling of a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            read_transaction_file("nonexistent_file.txt")

if __name__ == '__main__':
    unittest.main()