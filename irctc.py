import mysql.connector
class IRCTC:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="hit")
        self.cursor = self.conn.cursor()
        self.user_menu()
    
    def user_menu(self):
        user_input = input(""" Hi! How would you like to proceed?
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anything else to exit
        Enter your option: """)
        if user_input == '1':
            self.register()
        elif user_input == '2':
            self.login()
        else:
            print("Thanks for visiting!")

    def register(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        passwd = input("Enter Password: ")
        
        try:
           self.cursor.execute("INSERT INTO users(user_id, name, email, password) VALUES (NULL, '{}', '{}', '{}')".format(name,email,passwd))
            self.conn.commit()
        except mysql.connector.errors.IntegrityError as e:
            print("There is a user with same email")
        else:
            print("Voila! You're successfully registered!")

    def login(self):
        email = input("Enter Email: ")
        passwd = input("Enter Password: ")

        self.cursor.execute("SELECT * FROM users WHERE email='{}'".format(email))
        res = self.cursor.fetchall()
        if len(res)>0:
            if res[0][3] == passwd:
                print("You're successfully logged in!")
            else:
                print("Wrong Password! Try Again")
                self.login()
        else:
            print("You don't have a account here! Please register yourself!")
            self.register()


obj = IRCTC()