from core import JarvisCore
from router import Router

def main():
    router = Router()
    jarvis = JarvisCore(router)

    print("================================")
    print("       JARVIS CORE ONLINE")
    print("================================")
    print("Komendy: status, hello, exit")

    while True:
        try:
            user_input = input("\nYOU > ")

            if user_input.strip().lower() == "exit":
                print("JARVIS > Shutdown.")
                break

            jarvis.process(user_input)

        except KeyboardInterrupt:
            print("\nJARVIS > Shutdown.")
            break

if __name__ == "__main__":
    main()
