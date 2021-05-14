def countdown(x: int):
    if not x:
        print("Done")
        return x
    print(x, "...")
    countdown(x - 1)
    print(f"stack x={x}")


if __name__ == '__main__':
    countdown(5)
