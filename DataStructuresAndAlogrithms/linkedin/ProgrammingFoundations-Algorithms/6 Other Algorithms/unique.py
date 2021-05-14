if __name__ == '__main__':
    items = ["apple", "pear", "orange", "banana", "apple",
             "orange", "apple", "pear", "banana", "orange",
             "apple", "kiwi", "pear", "apple", "orange"]

    result = set(items)
    print(result)

    filter_ = dict()
    for item in items:
        filter_[item] = 0

    result = set(filter_.keys())
    print(result)
