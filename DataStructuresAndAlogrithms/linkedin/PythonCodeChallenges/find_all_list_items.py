def index_all(lst, item):
    indices = list()

    for i, el in enumerate(lst):
        if el == item:
            indices.append([i])
        elif isinstance(el, list):
            for index in index_all(el, item):
                indices.append([i] + index)
    return indices


if __name__ == '__main__':
    print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))
