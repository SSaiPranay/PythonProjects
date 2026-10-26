class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = balance

    def deposit(self, credit):
        if credit <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += credit
        return self.balance

    def withdraw(self, debit):
        if debit <= 0:
            raise ValueError("Withdrawal must be positive")

        if debit > self.balance:
            return "Insufficient Balance"

        self.balance -= debit
        return self.balance

    def get_balance(self):
        return self.balance



def surface_area_of_cube(edge_length: float) -> str:
    return 6 * edge_length ** 2

a=surface_area_of_cube(2)

print(a)
print(type(a))