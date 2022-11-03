from bankaccount import BankAccount

def main():
    account1 = BankAccount("Alex", 1000)
    account1.set_balance = -1000

    print(account1)

main()