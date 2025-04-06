# test/test_write.py
import unittest
import tempfile
import os
from src.write import write_new_current_accounts

class TestWriteNewCurrentAccounts(unittest.TestCase):

    def read_from_temp(self, accounts):
        tmp = tempfile.NamedTemporaryFile(delete=False, mode='r+', newline='')
        tmp.close()
        write_new_current_accounts(accounts, tmp.name)
        with open(tmp.name, 'r') as f:
            contents = f.readlines()
        os.unlink(tmp.name)
        return contents

    def test_valid_account_write(self):
        accounts = [{
            'account_number': '1',
            'name': 'John Doe',
            'status': 'A',
            'balance': 234.56,
            'plan': 'SP'
        }]
        lines = self.read_from_temp(accounts)
        self.assertIn("00001 John Doe           A 00234.56 SP\n", lines)
        self.assertTrue(lines[-1].startswith("00000 END_OF_FILE"))

    def test_invalid_account_number_raises(self):
        accounts = [{
            'account_number': 'abc',
            'name': 'John',
            'status': 'A',
            'balance': 100.00,
            'plan': 'NP'
        }]
        with self.assertRaises(ValueError):
            self.read_from_temp(accounts)

    def test_invalid_balance_too_high(self):
        accounts = [{
            'account_number': '12345',
            'name': 'John',
            'status': 'A',
            'balance': 100000.00,
            'plan': 'NP'
        }]
        with self.assertRaises(ValueError):
            self.read_from_temp(accounts)

    def test_invalid_plan_type(self):
        accounts = [{
            'account_number': '123',
            'name': 'John',
            'status': 'A',
            'balance': 100.00,
            'plan': 'ZZ'
        }]
        with self.assertRaises(ValueError):
            self.read_from_temp(accounts)

    def test_loop_multiple_accounts(self):
        accounts = [
            {'account_number': '1','name': 'A','status': 'A','balance': 10.0,'plan': 'SP'},
            {'account_number': '2','name': 'B','status': 'D','balance': 20.0,'plan': 'NP'}
        ]
        lines = self.read_from_temp(accounts)
        self.assertEqual(len(lines), 3)