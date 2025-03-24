class DailyUpdater:

    def updateAccount(self, Acounts, Transactions):
        current_acc_number = 0
        for transaction in Transactions:
            if transaction['transaction_code'] == '00':
                current_acc_number = self.login(Transactions)
            elif transaction['transaction_code'] == '01':
                self.withdrawal(current_acc_number, Acounts, Transactions)
            elif transaction['transaction_code'] == '02':
                self.transfer(current_acc_number, Acounts, Transactions)
            elif transaction['transaction_code'] == '03':
                self.paybill()
            elif transaction['transaction_code'] == '04':
                self.deposit()
            elif transaction['transaction_code'] == '05':
                self.create()
            elif transaction['transaction_code'] == '06':
                self.delete()
            elif transaction['transaction_code'] == '07':
                self.disable()
            elif transaction['transaction_code'] == '08':
                self.changeplan()
            elif transaction['transaction_code'] == '09':
                self.logout()



    def login(self, Transactions):
        return Transactions['account_number']

    def withdrawal(self, current_acc_number, Acounts, Transactions):
        pass

    def transfer(self, current_acc_number, Acounts, Transactions):
        pass

    def paybill(self):
        pass

    def deposit(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def disable(self):
        pass

    def changeplan(self):
        pass

    def logout(self):
        pass