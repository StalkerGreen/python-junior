import json
import os

NOTES_FILE = 'notes.json'
def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    try:
        with open(NOTES_FILE,"r", encoding="utf-8")as f:
            return json.load(f)
    except json.JSONDecodeError:
        print('Error 404: Notes file not found.'
              'Файл повреждён, начинаем с пустого списка.')
        return []
def save_notes(notes):
    with open(NOTES_FILE, 'w', encoding="utf-8")as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)
def add_note(notes):
    text = input("Введите текст заметки: ").strip()
    if not text:
        print("Заметка не может быть пустой.")
        return
    notes.append(text)
    print("Заметка добавлена.")
def show_notes(notes):
    if not notes:
        print("Заметок пока нет.")
        return
    print("\nВаши заметки:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")
def delete_note(notes):
    show_notes(notes)

    if not notes:
        return
    try:
        number = int(input("Введите номер заметки для удаления: "))
    except ValueError:
        print("Ошибка: нужно ввести число.")
        return
    if not (1 <= number <= len(notes)):
        print(f"Ошибка: номер должен быть от 1 до {len(notes)}.")
        return
    removed = notes.pop(number - 1)
    print(f"Заметка удалена: «{removed}»")

def main():
    notes = load_notes()

    while True:
        print("\n--- Записная книжка ---")
        print("1 — добавить заметку")
        print("2 — показать все заметки")
        print("3 — удалить заметку")
        print("4 — выйти")

        choice = input("Выберите пункт: ").strip()
        if choice == "1":
            add_note(notes)
        elif choice == "2":
            show_notes(notes)
        elif choice == "3":
            delete_note(notes)
        elif choice == "4":
            save_notes(notes)
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
if __name__ == '__main__':
    main()
