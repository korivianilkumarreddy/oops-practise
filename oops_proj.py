class chatbook:
    def __init__(self):
        self.username = ' '
        self.password = ' '
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input(""" Welcome to Chat book !! How would you like to proceed ??
                           1. press 1 to signup
                           2. press 2 to signin
                           3. press 3 to write a post 
                           4. press 4 to message a frnd
                           5. press any other key to exit""")
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        else :
            exit()    
    # signup function created......
    def signup(self):
        email = input("enter your email----->")
        pwd = input("set-up your password")
        self.username = email
        self.password = pwd
        print("\n")
        print("signed up successfully")
        print("\n")
        self.menu()


obj = chatbook()            