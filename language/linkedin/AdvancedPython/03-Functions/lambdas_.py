# Use lambdas as in-place functions


def celsius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9


def main():
    c_temps = [0, 12, 34, 100]
    f_temps = [32, 65, 100, 212]

    # Use regular functions to convert temps
    print(list(map(fahrenheit_to_celsius, f_temps)))
    print(list(map(celsius_to_fahrenheit, c_temps)))

    # Use lambdas to accomplish the same thing
    print(list(map(lambda t: (t - 32) * 5 / 9, f_temps)))
    print(list(map(lambda t: (t * 9 / 5) + 32, c_temps)))


if __name__ == "__main__":
    main()
