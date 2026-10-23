def withdraw(balance, amount):
    if amount <= 0:
        return "Invalid withdraw amount"

    # The Rule is, only allow withdrawal of the amount in balance or less
    # than the balance
    if amount > balance:
        return "Not enough money"

    balance -= amount

    return f"You withdraw ${amount:,.2f}"

def deposit(amount):
    if amount <= 0:
        return "Invalid deposit amount"

    balance += amount

    return f"You deposited ${amount:,.2f}"

def get_balance(balance):
    return f"Current Balance ${balance:,.2f}"

def main():
    # Let's start the program with $100
    balance = 100

    # How can we add a loop to continue the menu running until we quit
    while True:
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Balance")
        print("4. Quit")

        option = input("Select an Action (1-4): ")

        if option == "1":
            print(get_balance(balance))
            
            try:
                amount = float(input("Enter Withdraw Amount: "))
            except ValueError:
                print("Invalid Amount")
                continue
            
            print(withdraw(balance, amount))        
        elif option == "2":
            print(get_balance(balance))

            try:
                amount = float(input("Enter Deposit Amount: "))
            except ValueError:
                print("Invalid Amount")
                continue
            
            print(deposit(balance, amount)) 
        elif option == "3":
            print(get_balance(balance))
        elif option == "4":
            print("Thank you for using my ATM")
            break
        else:
            print("Invalid Option")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Your forcefully quitted the ATM App")