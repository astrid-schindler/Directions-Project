directions_list1 = ["NORDEN", "OSTEN", "WESTEN", "SUEDEN", "WESTEN", "WESTEN", "NORDEN"]

directions_list2 = ["SUEDEN", "NORDEN", "SUEDEN", "WESTEN", "WESTEN", "OSTEN", "NORDEN", "NORDEN", "OSTEN", "OSTEN"]


def solve(directions):

    norden = "NORDEN"
    sueden = "SUEDEN"
    osten = "OSTEN"
    westen = "WESTEN"

    for i in directions:
        if i == norden:
            for j in directions:
                if j == sueden:
                    directions.remove(norden)
                    directions.remove(sueden)

    for j in directions:
        if j == osten:
            for j in directions:
                if j == westen:
                    directions.remove(osten)
                    directions.remove(westen)

    return directions

