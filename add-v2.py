def add(prompt, strings):
    strings.append(input(prompt))
    return strings

ducks = ["Huey", "Dewey", "Louie"]

print(f" Ducks: {ducks}")
print()

add(" Add a duck: ", ducks)

print(f" Ducks: {ducks}")
print()

add(" Add a duck: ", ducks)

print(f" Ducks: {ducks}")
print()


composers = ["Mozart", "Bach"]
print(f" Composers: {composers}")
print()

add("Add a composer: ", composers)

print(f" Composers: {composers}")
print()
