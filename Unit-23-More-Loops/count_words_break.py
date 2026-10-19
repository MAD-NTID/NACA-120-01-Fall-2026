# The Goal of this program is to count how many times a word is matched

sentence = input("Enter a sentence: ")
sentence_split = sentence.split(" ")

# Loop infinitely until a word is found in the sentence
# if it does, exit
while True:
    word = input("Enter a word to find: ")

    if word in sentence_split:
        print("The word was found! Exiting")
        break    
    else:
        print("The word was not found")

    # spacing
    print()