from .fileHandler import FileHandler
from .Update import DailyUpdater
class BackEnd:
	def __init__(self):
		self.accounts = []
		self.transactions = []
		self.file_handler = FileHandler()
		self.daily_updater = DailyUpdater()  
	def run(self):
		self.accounts = self.file_handler.readMasterBankAccountsFile()
		self.transactions = self.file_handler.readTransactionFile()
		self.file_handler.testAccounts(self.accounts)
		self.file_handler.testTransactions(self.transactions)
		self.daily_updater.updateAccount(self.accounts,self.transactions)
		self.file_handler.update_master_bank_accounts_file(self.accounts)
		self.file_handler.writeCurrentBankAccountsFile(self.accounts)
		


