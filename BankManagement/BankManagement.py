import datetime

class HDFCBank:
    def _init_(self):
        self.__maxamount = 20000
        self.__userlimit = 3
        self.__useramount = 0.0
        self.__transaction_limits = {
            'cash_deposit': {'per_transaction_limit': 100000, 'per_day_limit': 200000},
            'imps_transfer': {'per_transaction_limit': 500000, 'per_day_limit': 2000000},
            'neft_transfer': {'per_transaction_limit': 10000000, 'per_day_limit': 10000000},
            'upi_transfer': {'per_transaction_limit': 100000, 'per_day_limit': 100000},
            'third_party_transfer': {'per_transaction_limit': 5000000, 'per_day_limit': 5000000}
        }
        self.__transaction_history = []

    def withdraw(self, amount):
        try:
            for i in range(3):
                if amount > self.__maxamount:
                    raise maxamounterror
                else:
                    if self._useramount == self._maxamount:
                        print("Transaction for HDFC is done")
                        break
                    else:
                        self.__userlimit -= 1
                        if self.__userlimit == 0:
                            print("Transaction is done for HDFC")
                            print("Transaction limit of HDFC reached")
                            raise maxlimit
                        elif self._useramount == self._maxamount:
                            print("Limit passed ")
                            print("Transaction for HDFC is done")
                            raise maxamounterror
                        else:
                            self.__useramount += amount
                            self.__transaction_history.append((amount, datetime.datetime.now()))
                            print("Transaction is done for HDFC")
                            print("Transaction left are", self.__userlimit)
                            break
        except maxamounterror:
            print("Maximum Transaction limit for HDFC is 20000 ")
            exit()
        except maxlimit:
            print("Maximum Transaction limit for HDFC is 3 ")
            exit()

    def get_transaction_limits(self, transaction_type):
        return self.__transaction_limits.get(transaction_type)

    def set_transaction_limits(self, transaction_type, per_transaction_limit, per_day_limit):
        self.__transaction_limits[transaction_type] = {
            'per_transaction_limit': per_transaction_limit,
            'per_day_limit': per_day_limit
        }

    def get_transaction_history(self):
        return self.__transaction_history


class Axisbank:
    def _init_(self):
        self.__maxamount = 30000
        self.__userlimit = 5
        self.__useramount = 0.0
        self.__transaction_limits = {
            'cash_deposit': {'per_transaction_limit': 100000, 'per_day_limit': 200000},
            'imps_transfer': {'per_transaction_limit': 500000, 'per_day_limit': 2000000},
            'neft_transfer': {'per_transaction_limit': 10000000, 'per_day_limit': 10000000},
            'upi_transfer': {'per_transaction_limit': 100000, 'per_day_limit': 100000},
            'third_party_transfer': {'per_transaction_limit': 5000000, 'per_day_limit': 5000000}
        }
        self.__transaction_history = []

    def withdraw(self, amount):
        try:
            for i in range(5):
                if amount > self.__maxamount:
                    raise maxamounterror
                else:
                    if self._useramount == self._maxamount:
                        print("Transaction limit of Axisbank reached")
                        raise maxamounterror
                    else:
                        self.__userlimit -= 1
                        if self.__userlimit == 0:
                            print("Transaction is done for Axisbank")
                            print("Transaction limit of Axisbank reached")
                            raise maxlimit
                        elif self._useramount == self._maxamount:
                            print("Amount limit exceeded")
                            print("Transaction for Axisbank is done")
                            raise maxamounterror
                        else:
                            self.__useramount += amount
                            self.__transaction_history.append((amount, datetime.datetime.now()))
                            print("Transaction is done for Axisbank")
                            print("Transaction left are", self.__userlimit)
                            break
        except maxamounterror:
            print("Maximum Transaction limit for Axisbank is 30000 ")
            exit()
        except maxlimit:
            print("Maximum Transaction limit for Axisbank is 5 ")
            exit()

    def get_transaction_limits(self, transaction_type):
        return self.__transaction_limits.get(transaction_type)

    def set_transaction_limits(self, transaction_type, per_transaction_limit, per_day_limit):
        self.__transaction_limits[transaction_type] = {
            'per_transaction_limit': per_transaction_limit,
            'per_day_limit': per_day_limit
        }

    def get_transaction_history(self):
        return self.__transaction_history


def poly_obj(object, amount):
    object.withdraw(amount)


class ATM:
    def _init_(self):
        self.bankobject = None
        self.bankName = input("Press 1 for HDFC, 2 for Axis, or 3 to view transaction history:")
        if self.bankName == "1":
            self.bankobject = HDFCBank()
            self.func()
        elif self.bankName == "2":
            self.bankobject = Axisbank()
            self.func()
        elif self.bankName == "3":
            self.view_transaction_history()

    def func(self):
        amount = float(input("Enter the amount you want to withdraw:"))
        poly_obj(self.bankobject, amount)
        choice = input("Press y to continue and n to exit:")
        if choice == 'Y' or choice == 'y':
            self.func()
        elif choice == 'N' or choice == 'n':
            quit()

    def get_transaction_limits(self, bank_name, transaction_type):
        if bank_name == 'HDFC':
            return self.bankobject.get_transaction_limits(transaction_type)
        elif bank_name == 'Axis':
            return self.bankobject.get_transaction_limits(transaction_type)
        else:
            return None

    def set_transaction_limits(self, bank_name, transaction_type, per_transaction_limit, per_day_limit):
        if bank_name == 'HDFC':
            self.bankobject.set_transaction_limits(transaction_type, per_transaction_limit, per_day_limit)
        elif bank_name == 'Axis':
            self.bankobject.set_transaction_limits(transaction_type, per_transaction_limit, per_day_limit)

    def view_transaction_history(self):
        bank_name = input("Enter the bank name (HDFC or Axis):")
        transaction_type = input("Enter the transaction type (cash_deposit, imps_transfer, neft_transfer, upi_transfer, third_party_transfer):")
        if bank_name == 'HDFC':
            transaction_history = self.bankobject.get_transaction_history()
        elif bank_name == 'Axis':
            transaction_history = self.bankobject.get_transaction_history()
        else:
            transaction_history = []
        filtered_history = [t for t in transaction_history if t[0] == transaction_type]
        if len(filtered_history) == 0:
            print("No transaction history found for the specified bank and transaction type.")
        else:
            print("NO entries found for the specified bank and transaction type")
ATM()
