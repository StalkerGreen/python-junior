from database import Database

if __name__ == "__main__":
    db = Database()

    print("=" * 40)
    print("1. Все заметки (get_all_notes):")
    print("=" * 40)
    for row in db.get_all_notes():
        print(f"ID: {row['id']}, Текст: {row['text']}, Дата: {row['created_at']}")

    print("\n" + "=" * 40)
    print("2. Добавляем заметку (add_note):")
    print("=" * 40)
    new_id = db.add_note("Заметка через класс Database", "2026-11-17")
    print(f"Добавлена заметка с ID: {new_id}")

    print("\n" + "=" * 40)
    print("3. Проверяем, что заметка добавилась:")
    print("=" * 40)
    for row in db.get_all_notes():
        print(f"ID: {row['id']}, Текст: {row['text']}, Дата: {row['created_at']}")

    print("\n" + "=" * 40)
    print("4. Удаляем добавленную заметку (delete_note):")
    print("=" * 40)
    deleted = db.delete_note(new_id)
    print(f"Удалено строк: {deleted}")

    print("\n" + "=" * 40)
    print("5. Проверяем, что заметка удалилась:")
    print("=" * 40)
    for row in db.get_all_notes():
        print(f"ID: {row['id']}, Текст: {row['text']}, Дата: {row['created_at']}")

    db.close()
    print("\nСоединение закрыто. Тест завершён.")
