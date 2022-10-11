users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

def login(users):
        while True:
            user = input("User: ")
            password = input("Password: ")
            if user in users and password == users[user]:
                return(user)
                break
            else:
                print("Invalid username or password")




users1 = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
user1 = login(users1)
print(f"Welcome {user1}")

users2 = {"foo":"123", "bar":"hello", "foobar":"hello123"}
user2 = login(users2)
print(f"Welcome {user2}")
