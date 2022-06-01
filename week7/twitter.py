import re

url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
# print(f"Username: {username}")


# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")


# use re.sub to find and replace
# username = re.sub("https://twitter.com/", "", url)
# print(f"Username: {username}")

# add regex to re.sub
# username  start with http:// or https:// optional
# www. is optional
# username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")


# use re.search
# regex must start with https:// or http://
# www. optional, in a non capturing group
# twitter.com
# followed by any charaters for 1 or more in a capturing group

# if matches := re.search("^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print(f"Username: {matches.group(1)}")
# else:
#     print("Invalid")


if matches := re.search("^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
else:
    print("Invalid")
