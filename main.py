import itertools as itool

# LISTS
directions_list1 = ["NORDEN", "OSTEN", "WESTEN", "SUEDEN", "WESTEN", "WESTEN", "NORDEN"]
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


# FUNCTION COUNTS DIRECTIONS
def solve_second(directions_second):

    norden = directions_second.count("NORDEN")
    sueden = directions_second.count("SUEDEN")
    osten = directions_second.count("OSTEN")
    westen = directions_second.count("WESTEN")

    abs_hor = abs(norden - sueden)
    abs_ver = abs(osten - westen)

    directions_second.clear()

    # WRITES HORIZONTAL DIRECTIONS
    if norden > sueden:
        directions_second.append(abs_hor * ["NORDEN"])
    else:
        directions_second.append(abs_hor * ["SUEDEN"])

    # WRITES HORIZONTAL DIRECTIONS
    if osten > westen:
        directions_second.append(abs_ver * ["OSTEN"])
    else:
        directions_second.append(abs_ver * ["WESTEN"])

    directions_second = list(itool.chain(*directions_second))

    return directions_second


# TESTING FUNCTIONS
print(directions_list1)
print(solve_second(directions_list1))

