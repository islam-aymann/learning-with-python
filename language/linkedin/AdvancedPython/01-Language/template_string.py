from string import Template


def main():
    # Usual string formatting with format()
    str1 = "You're watching {0} by {1}.".format("Advanced Python",
                                                "Joe Marini")
    print(str1)

    # Use substitute method with keyword arguments
    # Substitute method has extra security precautions
    template = Template("You're watching ${title} by ${author}.")
    str2 = template.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)

    # Use substitute method with a dictionary
    data = {
        "author": "Joe Marini",
        "title": "Advanced Python"
    }

    str3 = template.substitute(data)
    print(str3)

    # Inline formatting with format string
    title = "Advanced Python"
    author = "Joe Marini"

    print(f"You're watching {title} by {author}.")


if __name__ == '__main__':
    main()
