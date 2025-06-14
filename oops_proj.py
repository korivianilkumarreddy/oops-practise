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
                           5. press any other key to exit\n""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
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

    # signin function created
    def signin(self):
        if self.username == ' ' and self.password == ' ':
            print("plz signup first by pressing 1 in the main menu")
        else:
            uname = input("enter your email/username here--->")
            pwd = input("Enter your password here--->")
            if self.username==uname and self.password==pwd:
                print("you have signedin successfully !!")
                self.loggedin = True
            else:
                print("plz input correct credentials..")
        print("\n")
        self.menu()            

        


obj = chatbook()            