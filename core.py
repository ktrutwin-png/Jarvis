class JarvisCore:
    def __init__(self, router):
        self.router = router

    def process(self, user_input):
        print(f"[CORE] Otrzymano: {user_input}")
        result = self.router.route(user_input)
        print(f"[CORE] Wynik: {result}")
        return result
