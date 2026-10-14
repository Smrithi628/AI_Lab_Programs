rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

print("Simple Reflex Agent")
location = "A"
while "Dirty" in rooms.values():
    print("Location:", location)
    if rooms[location] == "Dirty":
        print("Room is dirty. Cleaning...")
        rooms[location] = "Clean"
    elif location == "A":
        location = "B"
    else:
        location = "A"
    if "Dirty" not in rooms.values():
        print("All rooms are clean!")

print("\nGoal-Based Agent")
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}
location = "A"
goal = "Clean all rooms"
while "Dirty" in rooms.values():
    if rooms[location] == "Dirty":
        print("Cleaning room", location)
        rooms[location] = "Clean"
    elif location == "A":
        location = "B"
    else:
        location = "A"
print("Goal achieved:", goal)
print(rooms)

