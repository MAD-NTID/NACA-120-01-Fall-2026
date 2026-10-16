# Loops uses range with starting number at 1, ending at 10 (10 is not inclusive)
# This means 1 to 10
for i in range (1, 10):
    print(i)


# Loops uses range with starting number at 1, ending at 11 (11 is not inclusive)
# This means 1 to 10
for i in range (1, 11):
    print(i)

# Another way (optional)
for i in range (1, 10 + 1):
    print(i)


# Loops uses range with starting number at 0, ending at 20 inclusively (so 21 is stop)
# Essentially printing all even numbers
for i in range (0, 21, 2):
    print(i)


# Loops uses range with starting number at 30, ending at 0 inclusively (so -1 is stop)
# Must use the step function when starting with a high number counting down
# We use the step function with value of -1 to count down 1 by 1
for i in range (30, -1, -1):
    print(i)

# Loops using range with a stop number of 5 (5 not inclusive)
for i in range (5):
    print(i)