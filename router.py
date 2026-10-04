from modules.system import SystemModule
from modules.time import TimeModule


class Router:
    def __init__(self):
        self.system = SystemModule()
        self.time = TimeModule()

    def route(self, user_input):
        command = user_input.strip().lower()

        if command == "status":
            return self.system.status()

        if command == "hello":
            return self.system.hello()

        if command == "time":
            return f"Aktualna godzina: {self.time.get_time()}"

        return "Nie znam jeszcze tej komendy."
