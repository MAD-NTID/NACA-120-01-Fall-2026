# The Goal of this program is to count how many times a word is matched

sentence = input("Enter a sentence: ")
word = input("Enter a word to find: ")

sentence_split = sentence.split(" ")

# What do we need to keep the count?
word_count = 0

# Loop the groups from sentence_split and check if word matches
# if it does, increment variable by 1
for group in sentence_split:
    if word == group:
        word_count += 1

print(f"The word {word} was found in {sentence} {word_count} times")