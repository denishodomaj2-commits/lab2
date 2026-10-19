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

