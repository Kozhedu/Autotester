#задание 1

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


# наследуй класс от BankAccount и переопредели метод withdraw
class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
    
    def withdraw(self, amount):
        commission = amount * self.interest_rate
        return super().withdraw(amount + commission)


# пример использования
acc = BankAccount(1000)
print(acc.withdraw(100))          # вывод: 900

savings_acc = SavingsAccount(1000, 0.05)
print(savings_acc.withdraw(100))  # вывод: 895

#задание 2
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}.")


class SpiderMan(Person):
    def __init__(self, name):
        super().__init__(name)

    def introduce(self, with_identity=False):
        super().introduce()
        if with_identity == True:
            print('Но вы можете знать меня как Человека-паука.')
        # переопредели метод суперкласса, используя super()
				# добавь новое условие, используя with_identity
           


peter = SpiderMan("Питер Паркер")
peter.introduce(with_identity=True)  
# Привет, меня зовут Питер Паркер. Но вы можете знать меня как Человека-паука.