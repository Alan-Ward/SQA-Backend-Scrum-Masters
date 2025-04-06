# test/test_read.py
import unittest
import tempfile
import os
from src.read import read_old_bank_accounts

class TestReadOldBankAccounts(unittest.TestCase):

    def write_to_temp(self, content):
        tmp = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        tmp.write(content)
        tmp.close()
        return tmp.name

    def test_valid_account_line(self):
        content = "00001 John Doe            A 01234.56 0005 SP\n"
        path = self.write_to_temp(content)
        result = read_old_bank_accounts(path)
        os.unlink(path)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['account_number'], '1')
        self.assertEqual(result[0]['balance'], 1234.56)
        self.assertEqual(result[0]['plan'], 'SP')

    def test_invalid_length(self):
        content = "short line\n"
        path = self.write_to_temp(content)
        result = read_old_bank_accounts(path)
        os.unlink(path)
        self.assertEqual(result, [])

    def test_invalid_account_number(self):
        content = "abcd1 John Doe            A 01234.56 0005 NP\n"
        path = self.write_to_temp(content)
        result = read_old_bank_accounts(path)
        os.unlink(path)
        self.assertEqual(result, [])

    def test_invalid_balance_format(self):
        content = "00001 John Doe            A 0123456 0005 NP\n"
        path = self.write_to_temp(content)
        result = read_old_bank_accounts(path)
        os.unlink(path)
        self.assertEqual(result, [])

    def test_invalid_plan_type(self):
        content = "00001 John Doe            A 01234.56 0005 ZZ\n"
        path = self.write_to_temp(content)
        result = read_old_bank_accounts(path)
        os.unlink(path)
        self.assertEqual(result, [])