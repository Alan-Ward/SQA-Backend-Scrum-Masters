import unittest
from unittest.mock import MagicMock, patch
from src.BankBackend import BackEnd

class TestBackEnd(unittest.TestCase):
    def setUp(self):
        self.backend = BackEnd()
        # Patch dependencies
        self.backend.file_handler = MagicMock()
        self.backend.daily_updater = MagicMock()

    def test01_empty_data(self):
        """Test with empty account and transaction lists."""
        self.backend.file_handler.readMasterBankAccountsFile.return_value = []
        self.backend.file_handler.readTransactionFile.return_value = []

        self.backend.run()

        self.backend.file_handler.testAccounts.assert_called_once_with([])
        self.backend.file_handler.testTransactions.assert_called_once_with([])
        self.backend.daily_updater.updateAccount.assert_called_once_with([], [])
        self.backend.file_handler.update_master_bank_accounts_file.assert_called_once()
        self.backend.file_handler.writeCurrentBankAccountsFile.assert_called_once()

    def test02_valid_data(self):
        """Test with normal valid data."""
        accounts = [{'account_number': '12345'}]
        transactions = [{'type': 'DEP', 'amount': 100}]
        self.backend.file_handler.readMasterBankAccountsFile.return_value = accounts
        self.backend.file_handler.readTransactionFile.return_value = transactions

        self.backend.run()

        self.backend.daily_updater.updateAccount.assert_called_once_with(accounts, transactions)

    def test03_invalid_accounts(self):
        """Simulate testAccounts raising an error."""
        self.backend.file_handler.readMasterBankAccountsFile.return_value = [{'account_number': '12345'}]
        self.backend.file_handler.readTransactionFile.return_value = []

        self.backend.file_handler.testAccounts.side_effect = Exception("Invalid accounts")

        with self.assertRaises(Exception) as context:
            self.backend.run()

        self.assertEqual(str(context.exception), "Invalid accounts")

    def test04_invalid_transactions(self):
        """Simulate testTransactions raising an error."""
        self.backend.file_handler.readMasterBankAccountsFile.return_value = [{'account_number': '12345'}]
        self.backend.file_handler.readTransactionFile.return_value = [{'type': 'DEP'}]

        self.backend.file_handler.testTransactions.side_effect = Exception("Invalid transaction")

        with self.assertRaises(Exception) as context:
            self.backend.run()

        self.assertEqual(str(context.exception), "Invalid transaction")

    def test05_loop_coverage_multiple_transactions(self):
        """Loop coverage: multiple transactions processed."""
        accounts = [{'account_number': '11111'}]
        transactions = [{'type': 'DEP'}, {'type': 'WDR'}, {'type': 'XFR'}]
        self.backend.file_handler.readMasterBankAccountsFile.return_value = accounts
        self.backend.file_handler.readTransactionFile.return_value = transactions

        self.backend.run()

        self.backend.daily_updater.updateAccount.assert_called_once_with(accounts, transactions)

if __name__ == '__main__':
    unittest.main()
