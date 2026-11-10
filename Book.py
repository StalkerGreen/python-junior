class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def info(self):
        return f"{self.title} — {self.author} {self.year}"
    def __str__(self):
        return self.info()


if __name__ == "__main__":
    book1 = Book("Война и мир", "Лев Толстой", 1869)
    book2 = Book("1984", "Джордж Оруэлл", 1949)

    print(book1.info())
    print(book2.info())
    print(book1)
    print(book2)

    print(f"Название первой книги: {book1.title}")
    print(f"Автор второй книги: {book2.author}")