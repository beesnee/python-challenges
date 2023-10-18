people = {
    "albert" : "Einstein",
    "charles" : "Darwin",
    "james" : "Cook",
    "andrew" : "Garfield"
}

print("Welcome to Who's Your Daddy!")
name = input("Enter a name and we will tell you the last name: ")
name_lower = name.lower()

if name_lower in people:
    print(people[name_lower])
    
else:
    print("That name is not avalible. Try again")

