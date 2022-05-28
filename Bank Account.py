class Account:
    def __init__(self):
        self.balance += value
        self.transactions.append(['Deposit', value])

    def deposit(self, value):
        self.balance += value
        self.transactions.append(['Deposit', value])

    def withdraw(self, value):
        if self.balance - value >= 10000:
            self.balance -= value
            self.transactios.append(['withdraw', value])
            return True
        else:
            return False

    def LastTransactions(self, n):
        return self.transactions[-1, (n + 1), -1]

    def __str__(self):
        return f"Account with {self.balance}balance({self.balance - 10000} withdrawable)"

a = Account()
a.deposit(10000)
a.deposit(50000)
a.withdraw(100000)
print(a)
print(*a.LastTransactions(10) , sep = '\n')