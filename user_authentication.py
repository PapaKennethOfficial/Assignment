def register():
    name = input("Enter your full name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    telephone = int(input("Enter phone number: "))
    return name,email,password,telephone

def pass_reset():
    new_password = input("Enter new password: ")
    confirm_password = input("confirm password: ")
    if new_password == confirm_password:
        print("Password reset successful")
        return new_password
    else:
        print("Passwords do not match. please try again.")
        return None

def google():
    user_name = input("Enter your user name: ")
    password = input("Enter password: ")
    return user_name, password

def facebook():
    user_name = input("Enter your user name: ")
    password = input("Enter password: ")
    return user_name, password

def login():
    email = input("Enter email: ")
    password = input("Enter password: ")
    return email, password

def valid(user_email, user_password):
    stored_email = "mensah@gmail.com"
    stored_password = "mensah233"
    if user_email == stored_email and user_password == stored_password:
        print("User logged in succefully")
        return True
    else:
        return False

print("KENSTECHY FORM REGISTRATION")
member = input("Already a member? yes or no \n").lower()
if member == "yes":
        email, password = login()
        if valid(email, password):
            print("Welcome back!")
 
        else:
            print("Login failed \n")
            pass_forget = input("Forgot password? yes or no").lower()
            if pass_forget == "yes":
                new_password = pass_reset()
                if new_password:
                    print("Please login with your new password")
            else:
                print("Exiting...")    
         
else:
    new_member = input("Want to register? yes or no \n").lower()
    if new_member == "yes":
        name, email,password, telephone = register()
        print("Regitration successful")
    else:
        facebook_user = input("Login via facebook? yes or no \n").lower()
        if facebook_user == "yes":
            facebook()
            print("Authentication done \nUser logged in successfully")
        else:
            google_user = ("Login via google? yes or no \n").lower()
            if google_user == "yes":
                google()
                print("Authentication done \nUser logged in successfully")
            else:
                print("Exit")
            