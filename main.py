from BankBackend import Backend
def main():
    backend = Backend()
    try:
        backend.run()
    except EOFError:
        pass

if __name__ == "__main__":
    main()