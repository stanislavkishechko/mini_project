from datetime import datetime

transactions = {}


def add_transaction(transaction_id: int, amount: float, date: datetime, category: str) -> None:
    if transaction_id in transactions:
        print(f"Транзакція з id {transaction_id} вже існує")
    else:
        transactions[transaction_id] = {
            "amount": amount,
            "date": date,
            "category": category,
        }
        print(f"Транзакція з id {transaction_id} успішно створена")


def edit_transaction(transaction_id: int, amount: float = None, date: datetime = None, category: str = None) -> None:
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
