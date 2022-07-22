directions_list1 = ["NORDEN", "OSTEN", "WESTEN", "SUEDEN", "WESTEN", "WESTEN", "NORDEN"]

directions_list2 = ["SUEDEN", "NORDEN", "SUEDEN", "WESTEN", "WESTEN", "OSTEN", "NORDEN", "NORDEN", "OSTEN", "OSTEN"]


def solve(directions):

    for i in directions:
        if i == "NORDEN":
            for j in directions:
                if j == "SUEDEN":
                    directions.remove("NORDEN")
                    directions.remove("SUEDEN")

    for k in directions:
        if k == "OSTEN":
            for m in directions:
                if m == "WESTEN":
                    directions.remove("OSTEN")
                    directions.remove("WESTEN")

    return directions


print(solve(directions_list2))
