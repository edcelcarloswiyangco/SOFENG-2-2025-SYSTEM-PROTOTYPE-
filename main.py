import log_in_and_sign_up as lo
import admin as ad
account = {}



while True:
    print("Welcome to our Booking a Barbers/shop ")
    print("1.Log in")
    print("2.Sign up")
    print("3.Log in as barber")

    choose = (input("Enter the number you Choose: ")).strip()
    if choose == '1':
        lo.login(account)
    elif choose == '2':
        lo.signup(account)
    elif choose == '3':
        lo.loginasbarber(account)
    elif choose == 'admin':
        attempts = 0
        while attempts < 3:
                adm= input("Enter the password of admin: ").strip().lower()
                if adm == ad.admin_password:
                    ad.admin()
                    break
                
                elif adm != ad.admin_password:
                    print("wrong password pls try again")
                    attempts+=1
        else:
            print("Too many failed attempts. Returning to the main menu.")            
                              
    else:
        print("Invalid choice")
    