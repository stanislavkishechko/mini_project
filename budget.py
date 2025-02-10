categories = {}


def create_budget_tracker(category: str, budget: int):
    spent = 0
    def tracker(amount):
        nonlocal spent
        spent += amount
        if spent >= budget:
            print(f"Бюджет на категорію {category} перевищено. Ліміт {budget}")
        else:
            print(f"Витрати в категорії {category}: {spent}/{budget}")
    return tracker
