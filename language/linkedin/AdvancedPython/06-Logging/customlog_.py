# Demonstrate how to customize logging output

import logging

ext_data = {'user': 'joem@example.com'}


def another_function():
    logging.debug("This is a debug-level log message", extra=ext_data)


def main():
    # set the output file and debug level, and
    # use a custom formatting specification
    fmt_str = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d " \
              "User:%(user)s %(message)s "
    date_str = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        format=fmt_str,
                        datefmt=date_str)

    logging.info("This is an info-level log message", extra=ext_data)
    logging.warning("This is a warning-level message", extra=ext_data)
    another_function()


if __name__ == "__main__":
    main()
