users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}

data = {"nisse":["luva", "vante"], "bosse":["spik", "skruv", "hammare"], "stina":["tidsmaskin"]}

print("Användare:")
print()
for key in users:
    print (f"{key}")
print()

print("Användare och lösenord:")
print()
for key in users:
    print (f"{key}) {users[key]}")
print()


print("Användare och deras data:")
print()
for key in data:
    print (f"{key}) {data[key]}")

användartest = input("Slå upp användare:")
if användartest in users:
    print(f"Data lagrat för {användartest}: {data[användartest]}")
else:
    print(f"Användaren {användartest} finns inte")
    
