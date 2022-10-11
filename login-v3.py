users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
options = {"r": "Try again", "q": "Quit"}

def login(users):
        while True:
            user = input("User: ")
            password = input("Password: ")
            
            if user in users and password == users[user]:
                return user
                break
            else:
                x = menu("Invalid username or password", "option: ", options)
                if x == "q":
                        return None
                


def menu(title, prompt, options):
    print()
    print(title)
    print()
    for key in options:
        print(f"{key}) {options[key]}")
        
    while True:
        selected_option = input(prompt)
        if selected_option in options:
            return (selected_option)
        
user = login(users)
