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
                           5. press any other key to exit
                           
                           -->""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
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

    # my_post function created
    def my_post(self):
        if self.loggedin == True:
            txt = input("enter your message here ->")
            print(f"following content has been posted-> {txt}")
        else:
            print("you need to signin first to post something...")
        print("\n")
        self.menu()

    # sendmsg function has created
    def sendmsg(self):
        if self.loggedin == True:
            txt = input("enter your message here->")
            frnd = input("whom to send the msg..?-->")
            print(f"your msg has been sent to {frnd}")
        else:
            print("you need to signin first to post something..")
        print("\n")
        self.menu()        


user1 = chatbook()            