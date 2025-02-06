i = 1
while i <= 5:
    print(i)
    i = i + 1
print("done")

p = 2
while p <= 5:
    print("*" * p)
    p = p + 1
print("doneeee")

balance = 1000  # Initial balance
attempts = 3  # Max number of failed attempts
password = "1234"

# User authentication loop
while attempts > 0:
    user_input = input("Enter your 4-digit PIN: ")
    
    if user_input == password:
        print("\nLogin successful! Welcome to your bank account.\n")
        
        # Main ATM menu loop
        while True:
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("\nEnter your choice (1-4): ")

            if choice == "1":
                print(f"\nYour current balance is: ${balance:.2f}\n")

            elif choice == "2":
                amount = float(input("Enter deposit amount: $"))
                if amount > 0:
                    balance += amount
                    print(f"\nSuccessfully deposited ${amount:.2f}. New balance: ${balance:.2f}\n")
                else:
                    print("\nInvalid deposit amount.\n")

            elif choice == "3":
                amount = float(input("Enter withdrawal amount: $"))
                if 0 < amount <= balance:
                    balance -= amount
                    print(f"\nSuccessfully withdrew ${amount:.2f}. Remaining balance: ${balance:.2f}\n")
                else:
                    print("\nInsufficient balance or invalid amount.\n")

            elif choice == "4":
                print("\nThank you for using the ATM. Goodbye!\n")
                break

            else:
                print("\nInvalid choice. Please select a valid option.\n")