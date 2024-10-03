
class BankAccount:

    def __init__(self, balance):
        self.balance= balance


    def add_money(self, amount):
        try:
            if amount >= 1:
                if amount > 0:
                    self.balance += amount
                    print(f"You have added: {amount} to your savings account")
                else:
                    print("Please add a valid amount, greater than 0.")
        except:
            print("Please add a valid amount, greater than 0.")
        return self.balance


    def withdraw_money(self, amount):
        self.balance -= amount
        return self.balance


class SavingsAccount(BankAccount):

    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw_money(self, amount):
        try:
            if amount >= 1:
                if self.balance - amount >= self.min_balance: 
                    self.balance -= amount
                    print(f"You have withdrew: {self.balance} from your savings account")
                else:
                    print("Not enough balance, to withdraw the amount you indicated.")
            else:
                print(f"The value {amount} to withdraw is not valid.")
        except Exception:
            print("Please enter a valid value.")
        return self.balance


my_account=SavingsAccount(100, 1)

print(f"You current balance is: {my_account.balance}")

my_account.add_money(1.1)

my_account.withdraw_money(20)

print(f"Your balance is now: {my_account.balance}")