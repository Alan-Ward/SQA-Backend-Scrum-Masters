import read
import readTransaction
import write
import updateMasterBankAccount

class FileHandler:
    def __init__(self):
        # since the files aren't yet loaded, it's initialized as null for now
        self.Accounts = None
        self.Transactions = None

    # loads transactions into an array of dictionaries
    def readTransactionFile(self):
        self.Accounts = readTransaction.read_transaction_file('Merged_Bank_Account_Transaction_File')

    # loads accounts into an array of dictionaries
    def readMasterBankAccountsFile(self):
        self.Transactions = read.read_old_bank_accounts('Master_Bank_Accounts_File')

    def writeCurrentBankAccountsFile(self):
        write.write_new_current_accounts(self.Accounts, 'New_Current_Bank_Accounts_File')

    def update_master_bank_accounts_file(self):
        updateMasterBankAccount.update_master_bank_accounts(self.Accounts, 'Master_Bank_Accounts_File')
