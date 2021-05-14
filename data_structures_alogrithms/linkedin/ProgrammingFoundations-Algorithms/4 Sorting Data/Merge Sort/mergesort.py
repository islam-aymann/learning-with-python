def merge_sort(dataset: list):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        left_arr = dataset[:mid]
        right_arr = dataset[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                dataset[k] = left_arr[i]
                i += 1
            else:
                dataset[k] = right_arr[j]
                j += 1

            k += 1

        while i < len(left_arr):
            dataset[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            dataset[k] = right_arr[j]
            j += 1
            k += 1


if __name__ == '__main__':
    items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print(items)
    merge_sort(items)
    print(items)
