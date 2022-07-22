directions_list1 = ["NORDEN", "OSTEN", "WESTEN", "SUEDEN", "WESTEN", "WESTEN", "NORDEN"]

directions_list2 = ["SUEDEN", "NORDEN", "SUEDEN", "WESTEN", "WESTEN", "OSTEN", "NORDEN", "NORDEN", "OSTEN", "OSTEN"]


def solve(directions):

    for i in directions:
        if i == "NORDEN":
            for j in directions:
                if j == "SUEDEN":
                    directions.remove("NORDEN")
                    directions.remove("SUEDEN")

    for j in directions:
        if j == "OSTEN":
            for j in directions:
                if j == "WESTEN":
                    directions.remove("OSTEN")
                    directions.remove("WESTEN")

    return directions


print(solve(directions_list2))