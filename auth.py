users_db = {}

def register_user(username: str, password: str) -> None:
    if username in users_db:
        print(f"Користувач {username} вже зареєстрований!")
    else:
        users_db[username] = hash(password)
        print(f"{username} зареєстрований")


def authentication_user(username: str, password: str) -> bool:
    if username in users_db:
        hashed_password = users_db[username]
        if hash(password) == hashed_password:
            print(f"Ласкаво просимо {username}")
            return True
        else:
            print(f"Невірний логін або пароль")
            return False
    else:
        print(f"Невірний логін або пароль")
        return False
