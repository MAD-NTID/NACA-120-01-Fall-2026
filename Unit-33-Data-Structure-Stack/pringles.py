"""
A Pringles program that demonstrates the use of Stack concepts.
"""

import stack

CHIP = "chip"
counts = 100

def main():
    # Let's Create a Pringles bottle
    for chip in range(counts):
        stack.push(f"{CHIP} - {chip}")

    stack.push(None)

    print(f"Pringles contains {stack.size()} chips")
    print(f"Pringles is empty? {stack.empty()}")
    print(f"What is the top chip in the pringles bottle? {stack.top()}")
    print()

    # Pop the top twice, should get 'chip - 99', 'chip - 98'
    print(f"Popped: {stack.pop()}")
    print(f"Popped: {stack.pop()}")
    print()

    print(f"Let's eat it all up!")

    for chip in range(stack.size()):
        print(f"I just ate {stack.pop()}")

    print()
    print(f"Pringles contains {stack.size()} chips")
    print(f"Pringles is empty? {stack.empty()}")
    print(f"What is the top chip in the pringles bottle? {stack.top()}")
    print()


if __name__ == "__main__":
    main()