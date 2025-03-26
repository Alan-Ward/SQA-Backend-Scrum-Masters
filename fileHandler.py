import read
import readTransaction
import write
import updateMasterBankAccount

class FileHandler:

    # loads transactions into an array of dictionaries
    def readTransactionFile(self):
        return readTransaction.read_transaction_file('Merged_Bank_Account_Transaction_File')

    # loads accounts into an array of dictionaries
    def readMasterBankAccountsFile(self):
        return read.read_old_bank_accounts('Master_Bank_Accounts_File')

    # writes updated Accounts to New_Current_Bank_Accounts_File
    def writeCurrentBankAccountsFile(self, Accounts):
        write.write_new_current_accounts(Accounts, 'New_Current_Bank_Accounts_File')

    # writes updates Master_Bank_Accounts_File with account info
    def update_master_bank_accounts_file(self, Accounts):
        updateMasterBankAccount.update_master_bank_accounts(Accounts, 'Master_Bank_Accounts_File')

    # prints contents of Accounts array
    def testAccounts(self, Accounts):
        for acc in Accounts:
            print(acc['account_number'], acc['name'], acc['status'], acc['balance'], acc['total_transactions'],acc['account_plan'])

    # prints contents of Transactions array
    def testTransactions(self, Transactions):
        for transaction in Transactions:
            print(transaction['transaction_code'], transaction['name'], transaction['account_number'],transaction['transaction_amount'])

