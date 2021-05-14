from collections import defaultdict

if __name__ == '__main__':
    items = ["apple", "pear", "orange", "banana", "apple",
             "orange", "apple", "pear", "banana", "orange",
             "apple", "kiwi", "pear", "apple", "orange"]

    counter = dict()

    for item in items:
        if item in counter.keys():
            counter[item] += 1
        else:
            counter[item] = 1
    print(counter)

    counter2 = defaultdict(int)

    for item in items:
        counter2[item] += 1

    print(counter2)
