import stack

if __name__ == '__main__':
    string = "123456789"
    reversed_string = ""
    s = stack.Stack()

    for c in string:
        s.push(c)

    while not s.is_empty():
        reversed_string += s.pop()

    print(reversed_string)
