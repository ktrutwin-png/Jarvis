from modules.system import SystemModule

class Router:
    def __init__(self):
        self.system = SystemModule()

    def route(self, user_input):
        command = user_input.strip().lower()

        if command == "status":
            return self.system.status()

        if command == "hello":
            return self.system.hello()

        return "Nie znam jeszcze tej komendy."
