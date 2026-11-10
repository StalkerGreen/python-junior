class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def info(self):
        return f"{self.title} — {self.author}, {self.year}"
    def __str__(self):
        return self.info()

    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Год должен быть положительным числом")
        self._year = value


class EBook(Book):
    def __init__(self,title,author,year,file_size):
        super().__init__(title,author,year)
        self.file_size = file_size

    def info(self):
        base = super().info()
        return f"{base} (файл: {self.file_size} МБ)"


########################################################################################

if __name__ == "__main__":
    book1 = Book("Война и мир", "Лев Толстой", 1869)
    book2 = Book("1984", "Джордж Оруэлл", 1949)

    print(book1.info())
    print(book2.info())
    print(book1)
    print(book2)

    print(f"Название первой книги: {book1.title}")
    print(f"Автор второй книги: {book2.author}")

    ebook = EBook("1984", "Джордж Оруэлл", 1949, 2.5)
    print(ebook.info())
    print(ebook)
    print(f"Размер файла: {ebook.file_size} МБ")
    print(f"Название: {ebook.title}")

# Проверка сеттера
book = Book("Тест", "Автор", 2000)
print(book.year)      # 2000
book.year = 2020
print(book.year)      # 2020

# Проверка ValueError
try:
    book.year = -5
except ValueError as e:
    print(f"Поймали ошибку: {e}")

# Проверка создания с некорректным годом
try:
    bad_book = Book("Плохая", "Книга", -1)
except ValueError as e:
    print(f"Поймали ошибку при создании: {e}")

