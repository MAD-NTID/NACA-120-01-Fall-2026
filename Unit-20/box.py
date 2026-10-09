import math

def box():
    print("========================================")
    print("||                                    ||")
    print("||                                    ||")
    print("||                                    ||")
    print("||                                    ||")
    print("||                                    ||")
    print("||                                    ||")
    print("========================================")


def aloha(word):
    # This one will print just as you typed it
    print("Hello " + word)

    # OR - This one will add spacing automatically after each ,

    print("Hello", word)

    # OR - This is called string formatting. Will learn later.

    print(f"Hello {word}")


def sum(num1, num2):
    result = num1 + num2
    return result


def main():
    box()

    aloha("RIT/NTID")

    print(sum(5, 10))

    # Better add context to explain what returned value is 
    print(f"10 + 5 = {sum(5, 10)}")

    # Or use the result for later use
    sum_result = sum(5, 10)
    print(f"10 + 5 = {sum_result}")

    # Find the result of 2 to the 10th power
    answer = math.pow(2, 10)
    print(f"2 to the power of 10 is {answer}")

    # What if I want to chain the results? Add 5 after
    answer = math.pow(2, 10) + 5
    print(f"2 to the power of 10 plus 5 is {answer}")

main()