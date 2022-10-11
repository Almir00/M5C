users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

while True:
    user = input("User: ")
    password = input("Password: ")
    if user in users and password == users[user]:
        print(f"Welcome {user}")
        break
    else:
        print("Invalid username or password")
        
