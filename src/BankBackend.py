from .fileHandler import FileHandler
from .Update import DailyUpdater
class BackEnd:
	def __init__(self):
		self.accounts = []
		self.transactions = []
	def run(self):
		self.master_accounts = FileHandler.readMasterBankAccountsFile()
		self.transactions = FileHandler.readTransactionFile()
		DailyUpdater.updateAccount(self.accounts,self.transactions)
		FileHandler.update_master_bank_accounts_file(self.accounts)
		FileHandler.writeCurrentBankAccountsFile(self.accounts)
		


