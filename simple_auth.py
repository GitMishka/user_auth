class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def authenticate(user, username, password):
    return user.username == username and user.password == password

# create a user
user = User("admin", "admin")

# try to authenticate
username = input("Enter username: ")
password = input("Enter password: ")

if authenticate(user, username, password):
    print("Authenticated")
else:
    print("Authentication failed")
