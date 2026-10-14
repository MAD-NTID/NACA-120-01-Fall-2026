def multiply(num1, num2):
    return num1 * num2

def main():
    num1 = int(input("Enter Num1 to Multiply: "))
    num2 = int(input("Enter Num2 to Multiply: "))

    result = multiply(num1, num2)

    # f is string formatter
    # {} is placeholder to put in the variables to convert to string (implicitly)
    print(f"{num1} * {num2} = {result}")

# This is the first function to be executed when this python file is run
if __name__ == "__main__":
    main()