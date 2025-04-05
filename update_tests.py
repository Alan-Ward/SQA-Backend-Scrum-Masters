import unittest
from src.updateMasterBankAccount import update_master_bank_accounts
import tempfile
import os

class TestUpdateMasterBankAccounts(unittest.TestCase):

    def setUp(self):
        # Create a temporary file to simulate the output file
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file_path = self.temp_file.name
        self.temp_file.close()

    def tearDown(self):
        os.remove(self.test_file_path)

    def test_TC1_ValidAccount(self):
        accounts = [{
            'account_number': '12345',
            'name': 'Alice',
            'status': 'A',
            'balance': 100.00,
            'total_transactions': 5,
            'plan': 'SP'
        }]
        try:
            update_master_bank_accounts(accounts, self.test_file_path)
        except Exception:
            self.fail("Valid account raised an exception.")

    def test_TC2_InvalidAccNum(self):
        accounts = [{
            'account_number': 12345,  # Should be str
            'name': 'Alice',
            'status': 'A',
            'balance': 100.00,
            'total_transactions': 5,
            'plan': 'SP'
        }]
        with self.assertRaises(ValueError):
            update_master_bank_accounts(accounts, self.test_file_path)

    def test_TC3_TooLongAccNum(self):
        accounts = [{
            'account_number': '1234567',  # > 5 digits
            'name': 'Alice',
            'status': 'A',
            'balance': 100.00,
            'total_transactions': 5,
            'plan': 'SP'
        }]
        with self.assertRaises(ValueError):
            update_master_bank_accounts(accounts, self.test_file_path)

    def test_TC4_LongName(self):
        accounts = [{
            'account_number': '12345',
            'name': 'A' * 21,  # > 20 chars
            'status': 'A',
            'balance': 100.00,
            'total_transactions': 5,
            'plan': 'SP'
        }]
        with self.assertRaises(ValueError):
            update_master_bank_accounts(accounts, self.test_file_path)

    def test_TC5_InvalidStatus(self):
        accounts = [{
            'account_number': '12345',
            'name': 'Alice',
            'status': 'X',  # Invalid status
            'balance': 100.00,
            'total_transactions': 5,
            'plan': 'SP'
        }]
        with self.assertRaises(ValueError):
            update_master_bank_accounts(accounts, self.test_file_path)

    def test_TC6_BadBalance(self):
        accounts = [{
            'account_number': '12345',
            'name': 'Alice',
            'status': 'A',
            'balance': -10.00,  # Negative balance
            'total_transactions': 5,
            'plan': 'SP'
        }]
        with self.assertRaises(ValueError):
            update_master_bank_accounts(accounts, self.test_file_path)

    def test_TC7_TooManyTx(self):
        accounts = [{
            'account_number': '12345',
            'name': 'Alice',
            'status': 'A',
            'balance': 100.00,
            'total_transactions': 10000,  # > 9999
            'plan': 'SP'
        }]
        with self.assertRaises(ValueError):
            update_master_bank_accounts(accounts, self.test_file_path)

    def test_TC8_InvalidPlan(self):
        accounts = [{
            'account_number': '12345',
            'name': 'Alice',
            'status': 'A',
            'balance': 100.00,
            'total_transactions': 5,
            'plan': 'XX'  # Invalid plan
        }]
        with self.assertRaises(ValueError):
            update_master_bank_accounts(accounts, self.test_file_path)

if __name__ == '__main__':
    unittest.main()