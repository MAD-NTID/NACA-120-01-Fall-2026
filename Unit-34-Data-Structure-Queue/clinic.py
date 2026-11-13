import my_queue as wait

# You go to a clinic, but there are people waiting in the waiting room
# Assume 2-3 people are already waiting, use Queue to sign yourself in


def main():
    wait.enqueue("John Smith")
    print("John Smith is now registerd and waiting")

    wait.enqueue("Jane Smith")
    print("Jane Smith is not registered and waiting")

    wait.enqueue("Analiese")
    print("Analiese entered the clinic and registered and is last")

    print(f"Count of people waiting is {wait.size()}")
    print(f"Is waiting room empty? {wait.empty()}")
    print(f"Front is {wait.front()} or peek {wait.peek()}")

    print(f"Nurse came to get a patient from waiting room: {wait.dequeue()}")
    print(f"Who's next now? {wait.peek()}")

    print(f"Nurse came to get a patient from waiting room: {wait.dequeue()}")
    print(f"Who's next now? {wait.peek()}")

    print(f"Count of people waiting is {wait.size()}")
    print(f"Is waiting room empty? {wait.empty()}")
    print(f"Front is {wait.front()} or peek {wait.peek()}")

    print(f"Nurse came to get a patient from waiting room: {wait.dequeue()}")
    print(f"Who's next now? {wait.peek()}")

    print(f"Count of people waiting is {wait.size()}")
    print(f"Is waiting room empty? {wait.empty()}")
    print(f"Front is {wait.front()} or peek {wait.peek()}")

if __name__ == "__main__":
    main()
