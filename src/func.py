def get_token():
    with open("config.txt", "r") as file:
        token = file.read()
        return token