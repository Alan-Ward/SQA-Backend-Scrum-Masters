from . import read
from . import readTransaction
from . import write
from . import updateMasterBankAccount
from pathlib import Path


class FileHandler:
    #Helper Function that returns the file path
    def findPath(self,filename):
        # Get the current script's directory
        current_dir = Path(__file__).parent

        # Go one directory up
        parent_dir = current_dir.parent

        # Construct the file path
        file_path = parent_dir / f"{filename}"

        return file_path
    # loads transactions into an array of dictionaries
    def readTransactionFile(self):
        file_path = self.findPath('Merged_Bank_Account_Transaction_File')
        return readTransaction.read_transaction_file(file_path)

    # loads accounts into an array of dictionaries
    def readMasterBankAccountsFile(self):
        file_path = self.findPath('Master_Bank_Accounts_File')
        return read.read_old_bank_accounts(file_path)

    # writes updated Accounts to New_Current_Bank_Accounts_File
    def writeCurrentBankAccountsFile(self, Accounts):
        file_path = self.findPath('New_Current_Bank_Accounts_File')
        write.write_new_current_accounts(Accounts, file_path)

    # writes updates Master_Bank_Accounts_File with account info
    def update_master_bank_accounts_file(self, Accounts):
        file_path = self.findPath('Master_Bank_Accounts_File')
        updateMasterBankAccount.update_master_bank_accounts(Accounts, file_path)

    # prints contents of Accounts array
    def testAccounts(self, Accounts):
        for acc in Accounts:
            print(acc['account_number'], acc['name'], acc['status'], acc['balance'], acc['total_transactions'],acc['account_plan'])

    # prints contents of Transactions array
    def testTransactions(self, Transactions):
        for transaction in Transactions:
            print(transaction['transaction_code'], transaction['name'], transaction['account_number'],transaction['transaction_amount'])

