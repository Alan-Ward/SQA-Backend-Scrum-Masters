from src.BankBackend import BackEnd
def main():
    backend = BackEnd()
    try:
        backend.run()
    except EOFError:
        pass
if __name__ == "__main__":
    main()