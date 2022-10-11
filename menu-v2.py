options1 = {"a":"Add item", "l":"List items", "q":"Log out"}

def menu(title, prompt, options):
    print(title)
    for key in options:
        print(f"{key}) {options[key]}")
       
    while True:
        selected_option = input(prompt)
        if selected_option in options:
            return (selected_option)   

options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
opt1 = menu("Select an action", "Action: ", options1)
print(f"You selected action {opt1}) {options1[opt1]}")
print()

options2 = {"r":"Try again", "q":"Quit"}
opt2 = menu("What do you want to do?", "My choice: ", options2)
print(f"You selected option {opt2}) {options2[opt2]}")
