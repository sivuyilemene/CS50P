# Exceptions

# SyntaxError
# ValueError
# NameError
def main():
    x = get_int("Whats x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            pass
            # print("x is not an integer, Please enter integers only")
        else:
            return x


main()
