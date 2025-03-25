import random


class DailyUpdater:

    def updateAccount(self, Accounts, Transactions):
        for transaction in Transactions:
            # responds to transaction code with appropriate function call
            if transaction['transaction_code'] == '01':
                self.withdrawal(Accounts, transaction)
            elif transaction['transaction_code'] == '02':
                self.transfer(Accounts, transaction)
            elif transaction['transaction_code'] == '03':
                self.paybill(Accounts, transaction)
            elif transaction['transaction_code'] == '04':
                self.deposit(Accounts, transaction)
            elif transaction['transaction_code'] == '05':
                self.create(Accounts, transaction)
            elif transaction['transaction_code'] == '06':
                self.delete(Accounts, transaction)
            elif transaction['transaction_code'] == '07':
                self.disable(Accounts, transaction)
            elif transaction['transaction_code'] == '08':
                self.changeplan(Accounts, transaction)
            elif transaction['transaction_code'] == '00':
                pass


    def withdrawal(self, Accounts, transaction):
        for acc in Accounts:
            if acc['account_number'] == transaction['account_number']:
                acc['balance'] -= transaction['transaction_amount']
                acc['balance'] -= self.calculate_fee(acc)
            return 0

    def transfer(self, Accounts, transaction):
        # TODO complete transfer method
        pass

    def paybill(self, Accounts, transaction):
        for acc in Accounts:
            if acc['account_number'] == transaction['account_number']:
                acc['balance'] -= transaction['transaction_amount']
                acc['balance'] -= self.calculate_fee(acc)
            return 0

    def deposit(self, Accounts, transaction):
        for acc in Accounts:
            if acc['account_number'] == transaction['account_number']:
                acc['balance'] += transaction['transaction_amount']
                acc['balance'] -= self.calculate_fee(acc)
            return 0

    def create(self,Accounts, transaction):
        Accounts.append({
            'account_number': self.generate_account_number(Accounts),
            'name': transaction['name'],
            'status': 'A',
            'balance': transaction['transaction_amount'],
            'total_transactions': 0
        })

    def delete(self, Accounts, transaction):
        pass

    def disable(self, Accounts, transaction):
        for acc in Accounts:
            if acc['account_number'] == transaction['account_number']:
                acc['status'] = 'D'
                # if calling the function a second time activates it again, just add if statement
            return 0

    def changeplan(self, Accounts, transaction):
        for acc in Accounts:
            if acc['account_number'] == transaction['account_number']:
                if acc['account_plan'] == 'NP':
                    acc['account_plan'] = 'SP'
                elif acc['account_plan'] == 'SP':
                    acc['account_plan'] = 'NP'
                else:
                    print("Account plan format wrong") # we can take this out during testing
            return 0


    def calculate_fee(self, acc):
        if acc['account_plan'] == 'SP':
            return 0.05
        elif acc['account_plan'] == 'NP':
            return 0.1
        else:
            return 0

    def generate_account_number(self, Accounts):
        # TODO needs to check if unique
        unique = False
        return random.randint(1,99999)
