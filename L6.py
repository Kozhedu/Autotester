class MyClass:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        # Этот метод имеет доступ к атрибутам экземпляра (self.value)
        return self.value

    @staticmethod
    def static_method(value):
        # Этот статический метод не имеет доступа к атрибутам экземпляра
        return value/2

# Создаем экземпляр класса
obj = MyClass(42)

# Вызываем метод экземпляра
result1 = obj.instance_method()
print(result1)  # Вывод: 42

# Вызываем статический метод класса
result2 = MyClass.static_method(42)
print(result2)  