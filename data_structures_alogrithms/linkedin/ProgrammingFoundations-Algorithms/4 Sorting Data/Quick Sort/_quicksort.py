def quicksort(dataset: list, first: int, last: int):
    if first < last:
        pivot_idx = partition(dataset, first, last)

        quicksort(dataset, first, pivot_idx - 1)
        quicksort(dataset, pivot_idx + 1, last)


def partition(data_values: list, first: int, last: int) -> int:
    pivot = data_values[first]
    lower = first + 1
    upper = last

    done = False
    while not done:
        while lower <= upper and data_values[lower] <= pivot:
            lower += 1

        while upper >= lower and data_values[upper] >= pivot:
            upper -= 1

        if upper < lower:
            done = True
        else:
            data_values[lower], data_values[upper] = data_values[upper], data_values[lower]

    data_values[first], data_values[upper] = data_values[upper], data_values[first]

    return upper


def main():
    items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    quicksort(items, 0, len(items) - 1)
    print(items)


if __name__ == '__main__':
    main()
