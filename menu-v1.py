options = {"a":"Add item", "l":"List items", "q":"Log out"}

def view(description, strings):
    print (description)
    print()
    for key in options:
        y = 0
        print(f"{key}) {options[key]}")
        y = y + 1
view("Select an action", options)


while True:
    selected_option = input("Option: ")
    if selected_option in options:
        print(f"You selected option {selected_option}) {options[selected_option]}")
        break
