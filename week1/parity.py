# Arithmetic Operators
# # % Modulus
# # Get User input
# x = int(input("Whats x? "))

# # if x is cleany divisible by 2, x is an even number
# if x % 2 == 0:
#   print("Even")
# else:
#   print("Odd")
def main():
    x = int(input("Whats x? "))
    if is_even(x):
        print("Even")
    else: 
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else: 
        return False

# def is_even(n):
#       return True if n % 2 == 0 else False


# def is_even(n):
#     return (n % 2 == 0)

main()
