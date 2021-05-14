import math


def change_making(denominations, target):
    cache = dict()

    def sub_problem(i, t):
        if (i, t) in cache:
            return cache[(i, t)]  # Memoization

        # Compute the lowest number of coins we need if choosing to take
        # a coin of the current denomination
        val = denominations[i]

        if val > t:
            # current denomination is too large
            choice_take = math.inf

        elif val == t:
            # target reached
            choice_take = 1
        else:
            # take and recurse
            choice_take = 1 + sub_problem(i, t - val)

        # Compute the lowest number of coins we need if not taking any more
        # coins of the current denomination.

        if i == 0:
            # not an option if no more denominations
            choice_leave = math.inf

        else:
            choice_leave = sub_problem(i - 1, t)

        optimal = min(choice_take, choice_leave)
        cache[(i, t)] = optimal
        return optimal

    return sub_problem(len(denominations) - 1, target)


if __name__ == '__main__':
    lst = [1, 5, 12, 19]
    target = 16
    print(f"change_making({lst}, {target}) = "
          f"{change_making(lst, target)}")

    lst = [25, 16, 5, 1]
    target = 33
    print(f"change_making({lst}, {target}) = "
          f"{change_making(lst, target)}")
