def get_red_envelope(budget, max_diff_rate=0.1, max_prefix_len=2):
    """Get a red envelope integer.

    >>> get_red_envelope(budget=10000)
    10000
    >>> get_red_envelope(budget=9500)
    10000
    >>> get_red_envelope(budget=5000)
    3600
    >>> get_red_envelope(budget=5000, max_diff_rate=0.2)
    6000
    >>> get_red_envelope(budget=66666, max_prefix_len=3)
    66600
    """
    max_amount = budget * (1 + max_diff_rate)
    lcuky_amounts = get_lucky_amounts(
        round(max_amount), max_prefix_len=max_prefix_len
    )
    min_diff_rate = 1
    last_amount = 0
    for amount in lcuky_amounts:
        diff = amount - budget
        diff_rate = abs(diff / budget)
        if diff_rate <= min_diff_rate:
            min_diff_rate = diff_rate
        else:
            return last_amount
        last_amount = amount
    return last_amount


def get_lucky_amounts(max_amount, max_prefix_len=2):
    lcuky_amounts = []
    for amount in range(1, max_amount + 1):
        if is_lucky(amount, max_prefix_len):
            lcuky_amounts.append(amount)
    return lcuky_amounts


def is_lucky(amount, max_prefix_len=2):
    if must_use_change(amount):
        return False
    if contains_4(amount):
        return False
    if prefix_is_odd_but_not_one(amount):
        return False
    if prefix_too_long(amount, max_prefix_len=max_prefix_len):
        return False
    if prefix_better_starts_with_6(amount):
        return False
    if contains_8(amount):
        return False
    if prefix_better_starts_with_10(amount):
        return False
    return True


def must_use_change(amount):
    min_bill = 100
    if amount % min_bill == 0:
        return False
    else:
        return True


def contains_4(amount):
    if "4" in str(amount):
        return True
    else:
        return False


def prefix_is_odd_but_not_one(amount):
    prefix = get_prefix(amount)
    if int(prefix) % 2 == 0:
        return False
    if prefix == "1":
        return False
    return True


def prefix_too_long(amount, max_prefix_len=2):
    prefix = get_prefix(amount)
    if len(prefix) > max_prefix_len:
        return True
    else:
        return False


def prefix_better_starts_with_6(amount):
    prefix = get_prefix(amount)
    if prefix.startswith("5"):
        return True
    if prefix.startswith("7"):
        return True
    return False


def contains_8(amount):
    if "8" in str(amount):
        return True
    else:
        return False


def prefix_better_starts_with_10(amount):
    prefix = get_prefix(amount)
    if prefix.startswith("9"):
        return True
    return False


def get_prefix(amount):
    prefix = str(amount).strip("0")
    return prefix


if __name__ == "__main__":
    import doctest

    doctest.testmod()
