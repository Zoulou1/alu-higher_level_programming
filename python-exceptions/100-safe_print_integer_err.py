#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(int(value)))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False

# Test cases
if __name__ == "__main__":
    import sys

    test_values = [89, -89, "89", '89', 89.9, 0, None, [89]]

    for value in test_values:
        has_been_print = safe_print_integer_err(value)
        if not has_been_print:
            print("{} is not an integer".format(value))
