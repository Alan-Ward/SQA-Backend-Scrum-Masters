from readTransaction import read_transaction_file
from print_error import log_constraint_error
from write import write_new_current_accounts
from read import read_old_bank_accounts
from Update import DailyUpdater
class BackEnd:
	def __init__(self):
		self.Accounts = []
		self.Transactions = []
	def run(self):
		self.Accounts = read_old_bank_accounts()
		self.Transactions = read_transaction_file()
		DailyUpdater.updateAccount(self.Accounts,self.Transactions)
		write_new_current_accounts(Accounts)


