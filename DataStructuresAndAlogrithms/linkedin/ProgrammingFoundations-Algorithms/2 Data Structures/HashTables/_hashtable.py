if __name__ == '__main__':
    items1 = dict({1: 1, "key2": 2, "key3": "three"})
    print(items1)

    items2 = dict(key1=1, key2=2, key3="three")
    print(items2)

    items3 = dict(key1=1, key2=2, key3="three")
    print(items3)

    items4 = {"key1": 1, "key2": 2, "key3": "three"}
    print(items4)

    items5 = dict()
    items5["key1"] = 1
    items5["key2"] = 2
    items5["key3"] = "three"
    print(items5)

    for key, value in items5.items():
        print(f"Key: {key}, value: {value}")
