from collections import deque

if __name__ == '__main__':
    queue = deque()

    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)

    print(queue)

    x = queue.popleft()
    print(x)
    print(queue)
