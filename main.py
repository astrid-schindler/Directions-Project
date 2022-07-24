# LISTS
directions_list1 = ["NORDEN", "OSTEN",  "WESTEN", "SUEDEN", "WESTEN", "WESTEN", "NORDEN"]
directions_list2 = ["SUEDEN", "NORDEN", "SUEDEN", "WESTEN", "WESTEN", "OSTEN", "NORDEN", "NORDEN", "OSTEN", "OSTEN"]


# FUNCTION REMOVES SENSELESS DIRECTIONS
def solve(directions):

    # REMOVES HORIZONTAL DIRECTIONS
    for i in directions:
        if i == "NORDEN":
            for j in directions:
                if j == "SUEDEN":
                    directions.remove("NORDEN")
                    directions.remove("SUEDEN")

    # REMOVES VERTICAL DIRECTIONS
    for k in directions:
        if k == "OSTEN":
            for m in directions:
                if m == "WESTEN":
                    directions.remove("OSTEN")
                    directions.remove("WESTEN")

    return directions


# REMOVES SIDE BY SIDE PAIRS
def solve_third(directions_third):

    for idx_a, a in enumerate(directions_third):
        if a == "NORDEN" and ((idx_a + 1) < len(directions_third)) and directions_third[idx_a + 1] == "SUEDEN":
            directions_third.pop(idx_a)
            directions_third.pop(idx_a)
            solve_third(directions_third)
        elif a == "SUEDEN" and ((idx_a + 1) < len(directions_third)) and directions_third[idx_a + 1] == "NORDEN":
            directions_third.pop(idx_a)
            directions_third.pop(idx_a)
            solve_third(directions_third)
        elif a == "OSTEN" and ((idx_a + 1) < len(directions_third)) and directions_third[idx_a + 1] == "WESTEN":
            directions_third.pop(idx_a)
            directions_third.pop(idx_a)
            solve_third(directions_third)
        elif a == "WESTEN" and ((idx_a + 1) < len(directions_third)) and directions_third[idx_a + 1] == "OSTEN":
            directions_third.pop(idx_a)
            directions_third.pop(idx_a)
            solve_third(directions_third)

    return directions_third


# TESTING FUNCTION
print(solve(directions_list2))
