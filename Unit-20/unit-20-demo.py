# Converting celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# Converting fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Is a number divisible by another number?
def is_divisible_by(num1, divisor):
    # think modulos.... remainder. 
    # it's like odd/even
    # how do we know it's perfectly divisible?
    # example - 2 / 2 = 0 (perfectly divisible)
    # example - 2 / 3 = not 0 (not perfectly divisble)
    result = num1 % divisor

    # hmmm. something's missing
    print(result)
    if result == 0:
        return True

    return False

print(f"2 divisible by 2? {is_divisible_by(2, 2)}") # true
print(f"2 divisible by 3? {is_divisible_by(2, 3)}") # false
print(f"42 divisible by 2? {is_divisible_by(42, 2)}") # true
print(f"42 divisible by 3? {is_divisible_by(42, 3)}") # true

print()

def is_divisible_by_simplified(num1, divisor):
    return num1 % divisor == 0

print(f"2 divisible by 2? {is_divisible_by_simplified(2, 2)}") # true
print(f"2 divisible by 3? {is_divisible_by_simplified(2, 3)}") # false
print(f"42 divisible by 2? {is_divisible_by_simplified(42, 2)}") # true
print(f"42 divisible by 3? {is_divisible_by_simplified(42, 3)}") # true