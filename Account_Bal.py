class Account():
    def __init__ (self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debited(self, amount):
        self.balance -= amount
        print("Rs.", amount, "debited from your account.")
        print("Total balance is ",self.balance)

    def credited(self, amount):
        self.balance += amount
        print("Rs.", amount, "credited to your account.")
        print("Total balance is ",self.balance)


acc1 = Account(10000, 334455)
acc1.debited(1000)
acc1.credited(500)