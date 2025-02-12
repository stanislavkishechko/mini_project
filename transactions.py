exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "UAH": 27.0
}

transactions = {}


def add_transaction(username: str, amount: float, date: str, category: str, currency: str = "USD") -> None:
    transaction_id = len(transactions) + 1
    if transaction_id in transactions:
        print(f"Транзакція з id {transaction_id} вже існує")
    else:
        converted_amount = amount * exchange_rates[currency]
        transactions[transaction_id] = {
            "username": username,
            "amount": converted_amount,
            "date": date,
            "category": category,
            "currency": currency,
        }
        print(f"Транзакція з id {transaction_id} успішно створена")


def edit_transaction(transaction_id: int, amount: float = None, date: str = None, category: str = None) -> None:
    if transaction_id in transactions:
        if amount:
            transactions[transaction_id]["amount"] = amount
        if date:
            transactions[transaction_id]["date"] = date
        if category:
            transactions[transaction_id]["category"] = category
        print(f"Транзакція з id {transaction_id} успішно редаговано")
    else:
        print("Транзакція з даним ID не знайдена")


def delete_transaction(transaction_id: int) -> None:
    if transaction_id in transactions:
        del transactions[transaction_id]
        print(f"Транзакція з id {transaction_id} успішно видалена")
    else:
        print("Транзакція з даним ID не знайдена")


def calculate_total_amount(category: str = None, index: int = 0, total: int = 0) -> float:
    keys = list(transactions.keys())
    if index == len(keys):
        return total
    if category:
        if transactions[keys[index]]["category"] == category:
            total += transactions[keys[index]]["amount"]
    else:
        total += transactions[keys[index]]["amount"]
    return calculate_total_amount(category, index + 1, total)


def view_balance(username: str) -> float:
    balance = sum([transaction["amount"] for transaction in transactions.values() if transaction["username"] == username])
    print(f"Ваш паточний баланс: {balance}")
    return balance

def generate_report(username: str) -> None:
    print(f"Звіт по транзакціям користувача {username}:")
    for transaction_id, transaction in transactions.items():
        if transaction["username"] == username:
            print(f"ID: {transaction_id}, Сума: {transaction['amount']}, Дата: {transaction['date']}, Категорія: {transaction['category']}")
