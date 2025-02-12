from transactions import add_transaction, view_balance, generate_report
from datetime_management import days_until_end_of_week, days_until_end_of_month
from auth import authentication_user, register_user
from budget import setup_category_budget


commands = {
    1: "Додати операцію",
    2: "Баланс",
    3: "Звіт",
    4: "Встановити бюджет",
    5: "Днів залишось",
    6: "Редагувати операцію",
    7: "Видалити оперцію",
    0: "Вийти"
}


def print_commands():
    print("Виберіть команду:")
    for command_id, command in commands.items():
        print(f"{command_id} - {command}")


def main():
    print("Вас вітає фінансовий трекер!")
    username = input("Введіть логін: ")
    password = input("Введіть пароль: ")
    if authentication_user(username, password):
        while True:
            print_commands()
            command = int(input("Введіть команду: "))
            if command == 1:
                amount = float(input("Введіть суму:"))
                date = input("Введіть дату (РРРР-ММ-ДД): ")
                category = input("Введіть категорію: ")
                currency = input("Введіть валюту: ")
                add_transaction(username, amount, date, category, currency)
            elif command == 2:
                view_balance(username)
            elif command == 3:
                generate_report(username)
            elif command == 4:
                category = input("Введіть категорію: ")
                budget = float(input(f"Встановіть бюджет для категорії {category}: "))
                setup_category_budget(category, budget)
            elif command == 5:
                days_until_end_of_month()
                days_until_end_of_week()
            elif command == 0:
                print("Вихід з системи")
                break
            else:
                print("Невідома команда. Спробуйте ще раз!")


if __name__ == "__main__":
    username = input("Введіть логін для реєстрації: ")
    password = input("Введіть пароль для реєстрації: ")
    register_user(username, password)
    main()
