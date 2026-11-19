username = input("Enter a username: ")
username_length = len(username)
stripped_username = username.strip()
lowercase_username = username.lower()
if stripped_username == "":
    print("Invalid username: it must not contain only spaces.")
elif username_length < 5:
    print("Invalid username: it must contain at least 5 characters.")
elif lowercase_username == "admin":
    print("Invalid username: 'admin' is reserved and cannot be used.")
else:
    print("Valid username: " + username)