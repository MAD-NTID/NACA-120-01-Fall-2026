def indexing():
    value = "Hello there, what do you plan to do?"

    print("\nIndexing")
    print("Original:", value)
    print("First Character value[0]:", value[0])
    print("Characteres at Specific Index value[12] > 'w':", value[13])
    print("Last Character is '?' value[-1]:", value[-1])
    print("Value's Length len(value):", len(value))


def slicing():
    value = "Hello there, what do you plan to do?"

    print("\nSlicing:")
    print("Original:", value)
    print("value[0:]:", value[0:])
    print("value[2:]:", value[2:])
    print("value[2:5]:", value[2:5])
    print("value[-1]:", value[-1])
    print("value[::-1]:", value[::-1])

def immutable():
    value = "Hello there, what do you plan to do?"
    
    print("\nImmutable:")
    print("Original:", value)

    try:
        # This is not ALLOWED
        value[0] = "h"
    except Exception as e:
        print("error - value[0] = 'h' is not allowed - string is immutable")
        print(e)

    print("Instead - Reconstruct the string")
    value = "h" + value[1:]

    print(value)
    print("Concatenating 'Bye!': " + value + "Bye")
    print("value is discarded and replaced with new string 'str' object")


def finding():
    value = "Hello there, what do you plan to do?"
        
    print("\nFinding:")
    print("Original:", value)

    print("Index of letter 't' is 6 > value.find('t'):", value.find('t'))
    print("No finding of match is -1 > value.find('ñ'):", value.find('ñ'))


def common():
    print("\nCommon Functions:")

    print("Upper all 'hello world'.upper():", 'hello world'.upper())
    print("Lower all 'HELLO WORLD'.lower():", 'HELLO WORLD'.lower())
    print("Capitalize first letter 'hello world'.capitalize():", 'hello world'.capitalize())
    print("Hello is Alpha True > 'Hello'.isalpha()", 'Hello'.isalpha())
    print("Hello is Alpha False > 'Hello2'.isalpha()", 'Hello2'.isalpha())
    print("1234 is Digit True > '1234'.isdigit()", '1234'.isdigit())
    print("A1234 is Digit False > 'A1234'.isdigit()", 'A1234'.isdigit())
    print("The in keyword to find a match 'hello' in ['hi', 'hello', 'hola'] > True:", 'hello' in ['hi', 'hello', 'hola'])

def interpolate():
    print("\nInterpolation:")

    value = 25.5

    # Preferred f-format much easier. UP to you
    print("Interpolation with 2 decimal places and f f'{value:.2f}':", f'{value:.2f}')
    print("Interpolation with 2 decimal places and % '{%.2f} % (value)'", '{%.2f}' % (value))


def string_iteration():
    value = "Hello there, what do you plan to do?"
            
    print("\nString Iteration:")
    print("Original:", value)

    # Before you can iterate, get the length of the string
    for index in range(len(value)):
        print(f"Letter at index {index}:", value[index])

    print("OR - even better and less coding")

    for letter in value:
        print(f"Letter: {letter}")

def main():
    indexing()

    slicing()

    immutable()

    finding()

    common()

    interpolate()

    string_iteration()

if __name__ == "__main__":
    try:
        main()
    except InterruptedError:
        print("Good bye.")
    