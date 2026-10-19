
# Лабораторна робота №2
# Система перегляду оцінок студентів

users = {
    "denys": {
        "password": "1234",
        "grades": [12, 10, 8, 11, 4, 9]
    },
    "andriy": {
        "password": "2222",
        "grades": [7, 5, 3, 10, 12, 8]
    },
    "ivan": {
        "password": "3333",
        "grades": [4, 2, 6, 9, 11, 5]
    },
    "maksym": {
        "password": "4444",
        "grades": [10, 12, 7, 3, 8, 6]
    }
}


def main():
    print("=== СИСТЕМА ПЕРЕГЛЯДУ ОЦІНОК ===")

    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    if login in users and users[login]["password"] == password:
        grades = users[login]["grades"]

        print("\nВхід успішний!")
        print("Ваші оцінки:", *grades)

        satisfactory = sum(1 for grade in grades if 5 <= grade <= 12)
        unsatisfactory = sum(1 for grade in grades if 1 <= grade <= 4)

        print("Кількість задовільних оцінок (5–12):", satisfactory)
        print("Кількість незадовільних оцінок (1–4):", unsatisfactory)

    else:
        print("\nПомилка! Неправильний логін або пароль.")


if __name__ == "__main__":
    main()
