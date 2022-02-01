from .helpers import get_prefix


def needs_to_use_change(price):
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


def prefix_starts_with_big_odd(price, big_odd=[5, 7, 9]):
    prefix = get_prefix(price)
    if prefix.startswith(tuple(str(odd) for odd in big_odd)):
        return True
    else:
        return False
