class Book:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def read(self, page):
        return f"Читаем книгу '{self.title}' - {self.content[page]}"

book = Book("Война и мир", ["Страница 1", "Страница 2", "Страница 3"])
print(book.read(1))   # Читаем книгу Война и мир - Страница 2 

class Audiobook(Book):
    def listen(self, page):
        super().__init__(self.title, self.content)
        return f'Воспроизводим страницу {self.content[page]} из аудиокниги {self.title}'

book = Book("Война и мир", ["Страница 1", "Страница 2", "Страница 3"])
print(book.read(1))          # Читаем книгу Война и мир - Страница 2

audiobook = Audiobook("1984", ["Страница 1", "Страница 2"])
print(audiobook.listen(0))   # Воспроизводим страницу 1 из аудиокниги 1984