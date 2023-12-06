def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(f"Hello, my name is {name}.")
    return badges

def assign_rooms(names):
    badges = []
    num = 1
    for name in names:
        badges.append(f"Hello, {name}! You'll be assigned to room {num}!")
        num += 1
    return badges

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)

    for name in assign_rooms(names):
        print(name)
    
    return
    
