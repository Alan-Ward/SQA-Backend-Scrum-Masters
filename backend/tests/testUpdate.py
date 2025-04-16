import unittest
from unittest.mock import patch
from src.Update import DailyUpdater

class TestDailyUpdater(unittest.TestCase):

    def setUp(self):
        self.updater = DailyUpdater()
        self.account = {
            'account_number': '12345',
            'name': 'Test',
            'status': 'A',
            'balance': 100.0,
            'total_transactions': 0,
            'plan': 'NP'
        }

    @patch('src.Update.print_error')
    def test_withdrawal(self, mock_print_error):
        transaction = {
            'account_number': '12345',
            'transaction_amount': 20.0
        }
        accounts = [self.account.copy()]
        self.updater.withdrawal(accounts, transaction)

        acc = accounts[0]
        expected_balance = 100.0 - 20.0 - 0.1
        self.assertEqual(acc['balance'], expected_balance)
        self.assertEqual(acc['total_transactions'], 1)

    @patch('src.Update.print_error')
    def test_transfer(self, mock_print_error):
        prev_transaction = {
            'transaction_code': '02',
            'account_number': '11111',
            'transaction_amount': 30.0
        }

        curr_transaction = {
            'transaction_code': '02',
            'account_number': '22222',
            'transaction_amount': 30.0
        }

        accounts = [
            {
                'account_number': '11111',
                'name':'test1',
                'status': 'A',
                'balance': 100.0,
                'total_transactions': 0,
                'plan': 'NP'
            },
            {
                'account_number': '22222',
                'name': 'test2',
                'status': 'A',
                'balance': 50.0,
                'total_transactions': 0,
                'plan': 'SP'
            }
        ]

        self.updater.transfer(accounts, curr_transaction, prev_transaction)

        sender = next(acc for acc in accounts if acc['account_number'] == '11111')
        receiver = next(acc for acc in accounts if acc['account_number'] == '22222')

        self.assertAlmostEqual(sender['balance'], 100.0 - 30.0 - 0.1)
        self.assertAlmostEqual(receiver['balance'], 50.0 + 30.0 - 0.05)
        self.assertEqual(sender['total_transactions'], 1)
        self.assertEqual(receiver['total_transactions'], 1)

    def test_paybill(self):
        transaction = {
            'account_number': '12345',
            'transaction_amount': 10.0
        }
        accounts = [self.account.copy()]
        self.updater.paybill(accounts, transaction)

        acc = accounts[0]
        self.assertAlmostEqual(acc['balance'], 100.0 - 10.0 - 0.1)
        self.assertEqual(acc['total_transactions'], 1)

    def test_deposit(self):
        transaction = {
            'account_number': '12345',
            'transaction_amount': 50.0
        }
        accounts = [self.account.copy()]
        self.updater.deposit(accounts, transaction)

        acc = accounts[0]
        self.assertEqual(acc['balance'], 149.9)
        self.assertEqual(acc['total_transactions'], 1)

    def test_delete(self):
        accounts = [self.account.copy()]
        self.updater.delete(accounts, {'account_number': '12345'})
        self.assertEqual(len(accounts), 0)

    def test_disable(self):
        accounts = [self.account.copy()]
        self.updater.disable(accounts, {'account_number': '12345'})

        self.assertEqual(accounts[0]['status'], 'D')

    def test_changeplan(self):
        accounts = [self.account.copy()]
        self.updater.changeplan(accounts, {'account_number': '12345'})

        # Should toggle between 'NP' and 'SP'
        self.assertEqual(accounts[0]['plan'], 'SP')

        self.updater.changeplan(accounts, {'account_number': '12345'})
        self.assertEqual(accounts[0]['plan'], 'NP')

if __name__ == '__main__':
    unittest.main()
