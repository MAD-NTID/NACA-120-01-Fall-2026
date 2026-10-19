# This variable for user's input
input_word = ""

while True:
    input_word = input("Enter a word: ").upper()

    print(f"Entered word {input_word}")

    if input_word == "EXIT":
        break

print("Done")