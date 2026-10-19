# This variable for user's input
input_word = ""

while input_word != "EXIT":
    input_word = input("Enter a word: ").upper()

    print(f"Entered word {input_word}")

print("Done")