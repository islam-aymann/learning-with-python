import time


def waiting_game():
    input("Your target time is 4 seconds\n"
          "---Press Enter to Begin after 4 seconds...")
    t1 = time.time()
    input()
    t = time.time() - t1
    print(t)


if __name__ == '__main__':
    waiting_game()
