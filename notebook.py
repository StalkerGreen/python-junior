import json
import os
from datetime import datetime

class Note:
    def __init__(self, text, created_at=None):# принимает text и опциональный created_at.
        self.text = text
        self.created_at = created_at or datetime.now().isoformat()# Если дата не передана — ставит текущую через datetime.now().isoformat(). Формат ISO ("2026-11-10T14:30:00") удобен для хранения.

    def __str__(self):
        return f"{self.text} (создано: {self.created_at})"# вывод: "Купить хлеб (создано: 2026-11-10T14:30:00)"

    def to_dict(self):# Превращает объект в словарь для json.dump. JSON не умеет хранить объекты Python, только словари/списки/строки/числа.
        return {"text": self.text, "created_at": self.created_at}#

    @classmethod # Создаёт объект Note из словаря (при загрузке из JSON). А cls — это сам класс Note (аналог self, но для класса). cls(...) вызывает __init__.
    def from_dict(cls, data):# Почему @classmethod, а не обычный метод? Потому что при загрузке у нас ещё нет объекта — мы его создаём. А from_dict — «фабрика» объектов.
        return cls(data["text"], data["created_at"])


class Notebook:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = self.load()
    def load(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open( self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            return [Note.from_dict(d)for d in data]
        except json.JSONDecodeError:
            print("Файл повреждён, начинаем с пустого списка.")
            return []
    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([note.to_dict() for note in self.notes], f, ensure_ascii=False, indent=2)
    def add(self, text):
        if not text.strip():
            print("Заметка не может быть пустой.")
            return
        note = Note(text.strip())
        self.notes.append(note)
        print(f"Заметка добавлена: «{note.text}»")
    def show(self):
        if not self.notes:
            print("Заметок пока нет.")
            return
        print("\nВаши заметки:")
        for i, note in enumerate(self.notes, start=1):
            print(f"{i}. {note}")
    def delete(self,number):
        if not self.notes:
            print("Заметок пока нет — нечего удалять.")
            return
        if not (1 <= number <= len(self.notes)):
            print(f"Ошибка: номер должен быть от 1 до {len(self.notes)}.")
            return
        removed = self.notes.pop(number - 1)
        print(f"Заметка удалена: «{removed.text}»")

def main():
    notebook = Notebook()

    while True:
        print("\n--- Записная книжка ---")
        print("1 — добавить заметку")
        print("2 — показать все заметки")
        print("3 — удалить заметку")
        print("4 — выйти")

        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            text = input("Введите текст заметки: ")
            notebook.add(text)
        elif choice == "2":
            notebook.show()
        elif choice == "3":
            notebook.show()
            if notebook.notes:
                try:
                    numbers = int(input("Введите номер заметки для удаления: "))
                    notebook.delete(numbers)
                except ValueError:
                    print("Ошибка: нужно ввести число.")
        elif choice == "4":
            notebook.save()
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()#2