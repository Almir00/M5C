strings = []
n = 5

print (f" n = {n}")

def add(prompt, strings):
    strings.append(input(prompt))
    return strings

def view(description, strings):
    print(description)
    print()
    x = 1
    for string in strings:
        print(f" {x}) {string}")
        x = x + 1
for _ in range(n):        
    add("Lägg till en sträng:", strings)
print()
view(f"Du har matat in följande {n} strängar", strings)
