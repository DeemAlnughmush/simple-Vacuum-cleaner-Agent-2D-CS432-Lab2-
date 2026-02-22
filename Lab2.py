# Lab 2  
# vacuum 2D

room_names = [
    ["A", "B"],
    ["C", "D"]
]

grid = [
    [1, 0],   # 1=Dirty, 0=Clean
    [1, 1]
]

path = [(0,0), (0,1), (1,1), (1,0)]  # top-left -> top-right -> bottom-right -> bottom-left
idx = 0
r, c = path[idx]

for step in range(1, 15): #14 steps

    location = room_names[r][c]   # get current room name
    status = "Dirty" if grid[r][c] == 1 else "Clean" # determine room status

    # Reflex rules
    if grid[r][c] == 1: # if it is dirty
        action = "Suck"
        grid[r][c] = 0
    else: # if it is clean
        action = "Move"
        idx = (idx + 1) % len(path) # move to next position in path  to keep index within path range 0-3 
        r, c = path[idx]

    print(f"Step {step}")
    print(f"Percept: [{location}, {status}]")
    print(f"Action: {action}")
    print("-" * 20)
    