# What is the Sum of all numbers from 10 to 0 = 55
loop_sum = 0
for i in range(11):
    loop_sum += i

print(loop_sum)

print()

def sum(n):
    print(n)

    # base case
    if(n == 0):
        return n

    # recursive case
    return n + sum(n - 1)


final_number = sum(10)
print(f"Final Number: {final_number}")