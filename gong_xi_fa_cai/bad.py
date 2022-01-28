from .helpers import get_prefix


def need_to_use_change(price):
    min_bill = 100
    if price % min_bill == 0:
        return False
    else:
        return True


def contains_4(price):
    if "4" in str(price):
        return True
    else:
        return False


def contains_8(price):
    if "8" in str(price):
        return True
    else:
        return False


def prefix_is_odd(price, not_odd=[1]):
    prefix = get_prefix(price)
    if int(prefix) % 2 == 0:
        return False
    if int(prefix) in not_odd:
        return False
    return True


def prefix_is_too_long(price, max_prefix_len=2):
    prefix = get_prefix(price)
    if len(prefix) > max_prefix_len:
        return True
    else:
        return False


def prefix_better_starts_with_6(price):
    prefix = get_prefix(price)
    if prefix.startswith("5"):
        return True
    if prefix.startswith("7"):
        return True
    return False


def prefix_better_starts_with_1(price):
    prefix = get_prefix(price)
    if prefix.startswith("9"):
        return True
    else:
        return False
