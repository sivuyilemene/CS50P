import re
# REGULAR EXPRESSION
# . this matches any character except a newline
email = input("Whats your email ").strip()


# # if "@" in email and "." in email:
# #   print("valid")
# # else:
# #   print("Invalid")


# # Split email into domain  and username
# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#   print("Valid")
# else:
#   print("Invalid")



# if re.search("^.+@.+\.edu$",email):
#   print("valid")
# else:
#   print("invalid")

# if re.search("^[^@]+@[^@]+\.edu$",email):
#   print("valid")
# else:
#   print("invalid")


# if re.search("^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
#   print("valid")
# else:
#   print("invalid")

# /w word character replaces [a-zA-Z0-9_]
# if re.search("^\w+@\w+\.edu$",email):
#   print("valid")
# else:
#   print("invalid")


# (A|B) creates a group of either B or A
# if re.search("^\w+@\w+\.(com|edu|net|gov)$",email):
#   print("valid")
# else:
#   print("invalid")

# flags
# A|B either A or B
# (...) creates group
# ignore case of user input
# if re.search("^\w+@\w+\.(com|edu|net|gov)$",email, flags=re.IGNORECASE):
#   print("valid")
# else:
#   print("invalid")

# (?...) optional
# any.word8@subdomain.domain.(com|edu|net|gov)
if re.search("^\w+@(\w+\.)?\w+\.(com|edu|net|gov)$",email, flags=re.IGNORECASE):
  print("valid")
else:
  print("invalid")