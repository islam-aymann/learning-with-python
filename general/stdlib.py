import operator


def main():
    a = [
        {"name": "islam", "age": 26},
        {"name": "ayman", "age": 21},
        {"name": "mohammed", "age": 22},
    ]

    print(list(map(operator.itemgetter("name", "age", "name"), a)))
    print(set(map(operator.itemgetter("name", "age", "name"), a)))


if __name__ == '__main__':
    main()
