# # get input from user and convert to int
# x = int(input('whats x? '))
# y = int(input("whats y? "))

# # print output
# print(f"Added two integers. Result: {x+y}")


# # FLOATS
# # numbers with decimal points need to  

# # get input from user and convert to float
# x = float(input('whats x? '))
# y = float(input("whats y? "))


# z = round(x + y)
# # print output
# print(f"Added two floats. Result: {z}")

# # format number to add commas 
# print(f"{z:,}")

# # Division
# z = round( x/y )
# print(f"Quotient of two floats. Result:{z} ")

def main():
    x = int(input("whats x? "))
    print("x squared is: ", square(x))

# Function to calculate square of a number
def square(num):
   return num ** 2
#  return pow(num, 2)
#  return num*num

if __name__ == "__main__":
    main()
