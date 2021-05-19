def str_compression(string):
    counter = dict()

    for char in string:
        counter[char] = counter.get(char, 0) + 1

    return ''.join([f'{k}{v}' for k, v in counter.items()])


if __name__ == '__main__':
    print(str_compression('AAAABBBBCCCCCDDEEEE'))
    print(str_compression('AAB'))
