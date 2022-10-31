accounts = {"user": "password", "user2": "password2"}
login_or_signup = input("Login or signup? ")

while True:
    if login_or_signup.upper() == 'LOGIN':
        username = input("Enter your username: ")
        if username in accounts:
            password = input("Enter your password: ")
            if accounts[username] == password:
                print("Logged in successfully.")
            else:
                print("Account credentials do not match.")
        else:
            print("Account not found.")
    elif login_or_signup.upper() == "SIGNUP":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        accounts[username] = password
