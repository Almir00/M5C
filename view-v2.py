names   = ["nisse", "stina", "bosse", "mimmi"]
animals = ["giraff", "myrslok", "tapir"]


def view(description, strings):
    print(description)
    print()
    x = 1
    for string in strings:
        print(f" {x}) {string}")
        x = x + 1

view("Lista med namn", names)
print()
view("Lista med djur", animals)
