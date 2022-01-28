def get_red_envelope(
    budget,
    max_error=0.1,
    false_odd_prefixes=["1"],
    max_prefix_len=2,
):
    """Get a red envelope integer.

    >>> get_red_envelope(budget=10000)
    10000
    >>> get_red_envelope(budget=9500)
    10000
    >>> get_red_envelope(budget=5000)
    3600
    >>> get_red_envelope(budget=5000)
    3600
    >>> get_red_envelope(budget=5000, max_error=0.2)
    6000
    >>> get_red_envelope(budget=66666, max_prefix_len=3)
    66600
    """
    max_price = round(budget * (1 + max_error))
    good_prices = get_good_prices(
        max_price,
        false_odd_prefixes=false_odd_prefixes,
        max_prefix_len=max_prefix_len,
    )
    return get_nearest_price(good_prices, budget)


def get_nearest_price(prices, target):
    sorted_prices = sorted(prices, key=lambda price: abs(price - target))
    return sorted_prices[0]


def get_good_prices(max_price, false_odd_prefixes=["1"], max_prefix_len=2):
    good_prices = []
    for price in range(1, max_price + 1):
        if is_good_price(
            price,
            false_odd_prefixes=false_odd_prefixes,
            max_prefix_len=max_prefix_len,
        ):
            good_prices.append(price)
    return good_prices


def is_good_price(price, false_odd_prefixes=["1"], max_prefix_len=2):
    if need_to_use_change(price):
        return False
    if contains_4(price):
        return False
    if contains_8(price):
        return False
    if prefix_is_odd(price, false_odd_prefixes=false_odd_prefixes):
        return False
    if prefix_is_too_long(price, max_prefix_len=max_prefix_len):
        return False
    if prefix_better_starts_with_6(price):
        return False
    if prefix_better_starts_with_1(price):
        return False
    return True


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


def prefix_is_odd(price, false_odd_prefixes=["1"]):
    prefix = get_prefix(price)
    if int(prefix) % 2 == 0:
        return False
    if prefix in false_odd_prefixes:
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


def get_prefix(price):
    prefix = str(price).rstrip("0")
    return prefix


if __name__ == "__main__":
    import doctest

    doctest.testmod()
