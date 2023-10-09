
def badge_maker(name):
    return f"Hello, my name is {name}."
badge_maker("Arel")

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(f"Hello, my name is {name}.")
    return badges

# names = ["Arel", "Carol"]
# badges = batch_badge_creator(names)
# print(badges)

def assign_rooms(names):
    room_assignments = []
    
    for index, name in enumerate(names, start=1):
        room_assignment = f"Hello, {name}! You'll be assigned to room {index}!"
        room_assignments.append(room_assignment)
    
    return room_assignments

# names = ["Arel", "Carol"]
# room_assignments = assign_rooms(names)
# print(room_assignments)


def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)
    
    for assignment in room_assignments:
        print(assignment)

# names = ["Arel", "Carol"]
#printer(names)