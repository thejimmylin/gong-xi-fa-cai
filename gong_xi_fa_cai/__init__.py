from .bad import (
    need_to_use_change,
    contains_4,
    contains_8,
    prefix_is_odd,
    prefix_is_too_long,
    prefix_better_starts_with_6,
    prefix_better_starts_with_1,
)
from .helpers import get_nearest_number


def is_good_price(price, not_odd=[1], max_prefix_len=2):
    """Return whether this price is a good red envelope price.

    Generally speaking, a red envelope price can't have an odd prefix, but 1
    is an exception.
    """
    if need_to_use_change(price):
        return False
    if contains_4(price):
        return False
    if contains_8(price):
        return False
    if prefix_is_odd(price, not_odd=not_odd):
        return False
    if prefix_is_too_long(price, max_prefix_len=max_prefix_len):
        return False
    if prefix_better_starts_with_6(price):
        return False
    if prefix_better_starts_with_1(price):
        return False
    return True


def get_good_prices(max_price, not_odd=[1], max_prefix_len=2):
    """Return a list of good red envelope prices."""
    good_prices = []
    for price in range(1, max_price + 1):
        if is_good_price(
            price,
            not_odd=not_odd,
            max_prefix_len=max_prefix_len,
        ):
            good_prices.append(price)
    return good_prices


def get_red_envelope(
    budget,
    max_error=0.1,
    not_odd=[1],
    max_prefix_len=2,
):
    """Return a good red envelope price within your budget.

    This is just a shortcut using `get_good_prices` and `get_nearest_number`
    to calculate what is your best choice.

    >>> get_red_envelope(budget=3000)
    3200
    >>> get_red_envelope(budget=3000, not_odd=[1, 3])
    3000
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
        not_odd=not_odd,
        max_prefix_len=max_prefix_len,
    )
    red_envelope = get_nearest_number(good_prices, budget)
    return red_envelope
