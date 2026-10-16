vowels = "aeiou"

if "a" in vowels:
    print("yes, it's a vowel")
else:
    print("no, it's not a vowel")
# yes, it's a vowel

if "b" in vowels:
    print("yes, it's a vowel")
else:
    print("no, it's not a vowel")

# no, it's not a vowel

# With User input
user_input = input("Enter a single character: ")

if user_input in vowels:
    print("Yes. Input in vowel")
else:
    print("No. Input not in vowel")