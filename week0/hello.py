def main():
  # Get user input
  name = input("what is your name? ")
  print(hello(name))

def hello(to="world"):
  # Say hello to user
  return f"hello, {to}" 


if __name__ == "__main__":
  main()
# # Remove whitspaces from str and capitalize the user's name
# name = name.strip().title()

# # Say hello to user
# print("hello", name)

# # formatting a string
# # print(f"hello , {name}")