import pyrebase
# pip3 install pyrebase4, normal pyrebase didn't seem to work
# pip install uplink if (collections.MutableMapping)

firebaseConfig = {
    'apiKey' : "AIzaSyAVqn91VbigCIrdcDXNLVNQU3b1h4ZLwOM",
    'authDomain' : "gencalendar-4818d.firebaseapp.com",
    'databaseURL': "https://gencalendar-4818d-default-rtdb.firebaseio.com",
    'projectId': "gencalendar-4818d",
    'storageBucket' : "gencalendar-4818d.appspot.com",
    'messagingSenderId' : "107573841336",
    'appId' : "1:107573841336:web:1aa0c09828438cd507534d",
    'measurementId' : "G-WQJ5ETVT2Y"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def login():
    print("Log in...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
    except:
        print("Invalid email or password")
    return

def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
    except:
        print("Email already exists")
    return

def logout():
    auth.current_user = None
    print("You have been logged out.")


while True:
    ans = input("Are you a new user? [y/n]: ")

    if ans == 'n':
        login()
        while True:
            ans = input("Do you want to sign out? [y/n]: ")
            if ans == 'y':
                logout()
                break  # breaks out of the inner loop
            elif ans == 'n':
                # maybe add more options here such as delete account.
                pass

    elif ans == 'y':
        signup()

    # Add an option to exit the program
    if input("Do you want to exit? [y/n]: ") == 'y':
        break  # breaks out of the outer loop

'''
ans = input("Are you a new user? [y/n]: ")

if ans == 'n':
    login()
    ans = input("Do you want to sign out? [y/n]: ")
    if ans == 'y':
        logout()
    elif ans == 'n':
        pass
elif ans == 'y':
    signup()
'''


