# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sport_teams = [("Royals", (18, 12)), ("Rockets", (24, 6)),
                   ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                   ("Kings", (15, 15)), ("Chargers", (20, 10)),
                   ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sorted_teams = sorted(sport_teams, key=lambda t: t[1][0], reverse=True)

    # create an ordered dictionary of the teams
    teams = OrderedDict(sorted_teams)
    print(teams)

    # Use popitem to remove the top item
    tm, wl = teams.popitem(last=False)
    print("Top team: ", tm, wl)

    # What are next the top 4 teams?
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    # test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    print("Equality test: ", a == b)

    # Note: in Python 3.7 dict element is ordered by default
    # and equality returns True even if order is not the same
    a = {"a": 1, "b": 2, "c": 3}
    b = {"a": 1, "c": 3, "b": 2}
    print(a, b)
    print("Equality test: ", a == b)


if __name__ == "__main__":
    main()
