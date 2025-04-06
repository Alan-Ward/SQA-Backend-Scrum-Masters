import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
from io import StringIO
import sys

from src.fileHandler import FileHandler

class TestFileHandler(unittest.TestCase):

    def setUp(self):
        # Create an instance of FileHandler
        self.file_handler = FileHandler()

        # Mock data for testing
        self.mock_accounts = [{
            'account_number': '12345',
            'name': 'John Smith',
            'status': 'A',
            'balance': 100.00,
            'total_transactions': 1,
            'plan': 'SP'
        }]
        self.mock_transactions = [{
            'transaction_code': '01',
            'name': 'John Smith',
            'account_number': '12345',
            'transaction_amount': 100.00
        }]

    def test_findPath(self):
        """Tests path construction"""
        result = self.file_handler.findPath('test.txt')
        self.assertIsInstance(result, Path)
        self.assertIn('test.txt', str(result))


    @patch('src.readTransaction.read_transaction_file')
    def test_readTransactionFile_success(self, mock_read_transaction):
        """Test successful reading of transaction file."""
        mock_read_transaction.return_value = [{"transaction_code": "01", "name": "John Smith", "account_number": "12345", "transaction_amount": 100.00}]
        transactions = self.file_handler.readTransactionFile()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["account_number"], "12345")

    @patch('src.readTransaction.read_transaction_file')
    def test_readTransactionFile_file_not_found(self, mock_read_transaction):
        """Test handling of missing transaction file."""
        mock_read_transaction.side_effect = FileNotFoundError("File not found")
        with self.assertRaises(FileNotFoundError):
            self.file_handler.readTransactionFile()

    @patch('src.read.read_old_bank_accounts')
    def test_readMasterBankAccountsFile_success(self, mock_read_accounts):
        """Test successful reading of master bank accounts."""
        mock_read_accounts.return_value = [{"account_number": "12345", "name": "John Smith", "balance": 500.00}]
        accounts = self.file_handler.readMasterBankAccountsFile()
        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0]["name"], "John Smith")

    @patch('src.write.write_new_current_accounts')
    def test_writeCurrentBankAccountsFile_success(self, mock_write_accounts):
        """Test successful writing of current bank accounts."""
        test_accounts = [{"account_number": "12345", "name": "John Smith", "balance": 500.00}]
        self.file_handler.writeCurrentBankAccountsFile(test_accounts)
        mock_write_accounts.assert_called_once_with(test_accounts, self.file_handler.findPath('New_Current_Bank_Accounts_File'))

    @patch('src.updateMasterBankAccount.update_master_bank_accounts')
    def test_update_master_bank_accounts_file_success(self, mock_update_master):
        """Test successful update of master bank accounts."""
        test_accounts = [{"account_number": "12345", "name": "John Smith", "balance": 500.00}]
        self.file_handler.update_master_bank_accounts_file(test_accounts)
        mock_update_master.assert_called_once_with(test_accounts, self.file_handler.findPath('Master_Bank_Accounts_File'))

    @patch('sys.stdout', new_callable=StringIO)
    def test_testAccounts(self, mock_stdout):
        """Test if testAccounts prints correctly."""
        test_accounts = [{"account_number": "12345", "name": "John Smith", "status": "A", "balance": 500.00, "total_transactions": 1, "plan": "S"}]
        self.file_handler.testAccounts(test_accounts)
        self.assertIn("12345 John Smith A 500.0 1 S", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_testTransactions(self, mock_stdout):
        """Test if testTransactions prints correctly."""
        test_transactions = [{"transaction_code": "01", "name": "John Smith", "account_number": "12345", "transaction_amount": 100.00}]
        self.file_handler.testTransactions(test_transactions)
        self.assertIn("01 John Smith 12345 100.0", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()