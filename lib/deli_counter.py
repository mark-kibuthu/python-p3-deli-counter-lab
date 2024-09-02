def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        current_line = "The line is currently:"
        for index, person in enumerate(katz_deli, start=1):
            current_line += f" {index}. {person}"
        print(current_line)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli.pop(0)}.")