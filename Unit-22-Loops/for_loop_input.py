times_to_loop = int(input("Enter # of times would you like to loop: "))
sum = 0

for count in range(times_to_loop):
    sum += count # this is the same as sum = sum + i
    print(count)

print(f"Final Sum is {sum}")