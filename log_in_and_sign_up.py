


def login(account):
    print("Please log in to your Account ")
    email = input("Enter your email here: ")
    password = input("Enter your password here: ")
    if email in account and account[email]['password'] == password:
        print("Log in is successfully ")
        return email
    else:
        print("Invalid username or password. Please try again.")
        return None
    
def signup(account):
    email = input("Enter your desire email: ").strip()
    if email in account:
        print("This email is Already owned by other ")
    else:
        password = input("Enter your password: ").strip()
        account[email] = {'password': password}
        print("Account created successfully!")

    

def loginasbarber(account):
    print("Please log in to your Account ")
    barber_email = input("Enter your email here: ").strip()
    password = input("Enter your password here: ").strip()
    if barber_email in account and account[barber_email]['password'] == password:
        print("Log in is successfully ")
        return barber_email
    else:
        print("Invalid username or password. Please try again.")
        return None
