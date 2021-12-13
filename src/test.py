def start():
    while True:
        try:
            _ = input("Foobar?")
            # Same process

        except KeyboardInterrupt:
            print("Interrupt")
            # Shutdown
            break


if __name__ == "__main__":
    start()
