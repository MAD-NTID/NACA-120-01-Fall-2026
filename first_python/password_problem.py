# Set a constant password topS3cret as the correct password
CORRECT_PASSWORD = "topS3cret"
password = input("Enter your password: ")

"""
    this works the same
    python is not picky about single or double quotes

    my comment first line
    my comment second line
    my comment third line
    my multi line comment block
"""
if (password == CORRECT_PASSWORD):
    print("Welcome Admin")
else:
    print("Invalid Username/Password")