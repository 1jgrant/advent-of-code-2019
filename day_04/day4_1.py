import re


def num_of_valid_passwords(start: int, stop: int) -> int:
    count = 0
    password = start
    while password < stop + 1:
        is_6_digits = len(str(password)) == 6
        if is_6_digits and has_two_adjacent_digits(password) and never_decreases(password):
            count += 1
        password += 1
    return count


def has_two_adjacent_digits(password: int) -> bool:
    return bool(re.search(r'(\d)\1', str(password)))


def never_decreases(password: int) -> bool:
    password_string = str(password)
    for i in range(len(str(password))):
        if i > 0:
            if password_string[i] < password_string[i-1]:
                return False
    return True


print(num_of_valid_passwords(130254, 678275))