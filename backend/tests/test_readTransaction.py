import unittest
import os
import tempfile

from src.readTransaction import read_transaction_file

class TestTransactionFileStatementCoverage(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        # Clean up temporary files
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    

    def test_invalid_length_line(self):
        """Tests a line with wrong length to hit the continue statement"""
        test_file = os.path.join(self.test_dir, "invalid_length.txt")
        with open(test_file, 'w') as f:
            f.write("This line is too short\n")  # Too short
            f.write("01 John Smith           12345 00100.000000000000000000000000\n")#Too long
        
        result = read_transaction_file(test_file)
        self.assertEqual(len(result), 0)  # Should skip invalid line

    def test_invalid_trans_code_format(self):
        """Tests a line with wrong length to hit the continue statement"""
        test_file = os.path.join(self.test_dir, "invalid_length.txt")
        with open(test_file, 'w') as f:
            f.write("A1 John Smith           12345 00100.00\n")  # Alpha Numeric
            f.write("99 John Smith           12345 00100.00\n")  # Code does not exist
            
        result = read_transaction_file(test_file)
        self.assertEqual(len(result), 0)  # Should skip invalid line

    def test_invalid_trans_amount_format(self):
        """Tests a line with wrong length to hit the continue statement"""
        test_file = os.path.join(self.test_dir, "invalid_length.txt")
        with open(test_file, 'w') as f:
            f.write("01 John Smith           12345 AZD23.AA\n") #Alpha numeric
            f.write("01 John Smith           12345 00100000\n") #Lacks a decimal point
        
        result = read_transaction_file(test_file)
        self.assertEqual(len(result), 0)  # Should skip invalid line

    def test_account_number_format(self):
        """Tests a line with wrong length to hit the continue statement"""
        test_file = os.path.join(self.test_dir, "invalid_length.txt")
        with open(test_file, 'w') as f:
            f.write("01 John Smith           AS-123 AZD23.AA\n") #Alpha numeric
        
        result = read_transaction_file(test_file)
        self.assertEqual(len(result), 0)  # Should skip invalid line

    def test_valid_transaction(self):
        """Tests happy path so only need to test for invalid transaction statement blocks after"""
        test_file = os.path.join(self.test_dir, "valid.txt")
        with open(test_file, 'w') as f:
            f.write("01 John Smith           12345 00100.00\n")  # 38 chars
        
        result = read_transaction_file(test_file)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['transaction_code'], '01')
        self.assertEqual(result[0]['name'], 'John Smith          ')


if __name__ == '__main__':
    unittest.main()