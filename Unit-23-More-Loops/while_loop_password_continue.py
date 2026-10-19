password = ""

while True:
    password = input("Enter the password: ")

    if password != "Shh$3cret":
        print("Password not matched!\n")
        continue

    break

print("Welcome admin, you are in!")