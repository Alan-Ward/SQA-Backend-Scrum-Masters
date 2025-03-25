import random


class DailyUpdater:

    def updateAccount(self, Accounts, Transactions):
        previous_transaction = None
        for transaction in Transactions:
            # responds to transaction code with appropriate function call
            if transaction['transaction_code'] == '01':
                self.withdrawal(Accounts, transaction)
            elif transaction['transaction_code'] == '02':
                self.transfer(Accounts, transaction, previous_transaction)
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
            previous_transaction = transaction

    #---------------------------------------------------------------------
    def withdrawal(self, Accounts, transaction):
        for acc in Accounts:
            if acc['account_number'] == transaction['account_number']:
                # the numbers are rounded to 2 decimal places for accuracy
                acc['balance'] -= transaction['transaction_amount']
                acc['balance'] -= self.calculate_fee(acc)
        return 0

    # ---------------------------------------------------------------------
    def transfer(self, Accounts, transaction, previous_transaction):
        # the prof mentioned that for transfer transactions, 2 transactions are recorded:
        # the first one from the sender
        # and the second one from the receiver
        # (they are always next to each other)
        # for this function, if the previous transaction isn't a transfer, it does nothing, but if this is the second transfer, both transactions are run
        if previous_transaction is not None and  previous_transaction['transaction_code'] == '02':
            for previous_acc in Accounts:
                if previous_acc['account_number'] == previous_transaction['account_number']:
                    print("previous")
                    previous_acc['balance'] -= previous_transaction['transaction_amount']
                    previous_acc['balance'] -= self.calculate_fee(previous_acc)

            for acc in Accounts:
                if acc['account_number'] == transaction['account_number']:
                    print("current")
                    acc['balance'] += transaction['transaction_amount']
                    acc['balance'] -= self.calculate_fee(acc)
        return 0

    # ---------------------------------------------------------------------
    def paybill(self, Accounts, transaction):
        for acc in Accounts:
            if acc['account_number'] == transaction['account_number']:
                acc['balance'] -= transaction['transaction_amount']
                acc['balance'] -= self.calculate_fee(acc)
        return 0

    # ---------------------------------------------------------------------
    def deposit(self, Accounts, transaction):
        for acc in Accounts:
            if acc['account_number'] == transaction['account_number']:
                acc['balance'] += transaction['transaction_amount']
                acc['balance'] -= self.calculate_fee(acc)

        return 0

    # ---------------------------------------------------------------------
    def create(self,Accounts, transaction):
        Accounts.append({
            'account_number': self.generate_account_number(Accounts),
            'name': transaction['name'].strip(),
            'status': 'A',
            'balance': transaction['transaction_amount'],
            'total_transactions': 0,
            'account_plan': 'NP'
        })

    # ---------------------------------------------------------------------
    def delete(self, Accounts, transaction):
        for acc in Accounts:
            if acc['account_number'] == transaction['account_number']:
                Accounts.remove(acc)
        return 0

    # ---------------------------------------------------------------------
    def disable(self, Accounts, transaction):
        for acc in Accounts:
            if acc['account_number'] == transaction['account_number']:
                acc['status'] = 'D'
                acc['balance'] -= self.calculate_fee(acc)
                # if calling the function a second time activates it again, just add if statement
        return 0

    # ---------------------------------------------------------------------
    def changeplan(self, Accounts, transaction):
        for acc in Accounts:
            if acc['account_number'] == transaction['account_number']:
                if acc['account_plan'] == 'NP':
                    acc['account_plan'] = 'SP'
                    acc['balance'] -= self.calculate_fee(acc)
                elif acc['account_plan'] == 'SP':
                    acc['account_plan'] = 'NP'
                    acc['balance'] -= self.calculate_fee(acc)
                else:
                    print("Account plan format wrong") # we can take this out during testing
        return 0

    # ---------------------------------------------------------------------
    def calculate_fee(self, acc):
        if acc['account_plan'] == 'SP':
            return 0.05
        elif acc['account_plan'] == 'NP':
            return 0.1
        else:
            return 0

    # ---------------------------------------------------------------------
    def generate_account_number(self, Accounts):
        # TODO needs to check if unique
        unique = False
        return random.randint(1,99999)
