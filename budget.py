categories = {}


def create_budget_tracker(category: str, budget: float):
    spent = 0
    def tracker(amount):
        nonlocal spent
        spent += amount
        if spent >= budget:
            print(f"Бюджет на категорію {category} перевищено. Ліміт {budget}")
        else:
            print(f"Витрати в категорії {category}: {spent}/{budget}")
    return tracker


def setup_category_budget(category: str, budget: float):
    categories[category] = create_budget_tracker(category, budget)
    print(f"Бюджет для категорії {category} встановлено на {budget}")
