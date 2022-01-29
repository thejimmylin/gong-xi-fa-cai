from . import bad_signs
from .helpers import get_nearest_number


class ReasonNotFound(Exception):
    pass


def get_why_bad(
    price,
    allow_needs_to_use_change=False,
    allow_contains_4=False,
    allow_contains_8=False,
    allow_prefix_is_odd=False,
    not_odd=[1],
    allow_prefix_is_too_long=False,
    max_prefix_len=2,
    allow_prefix_starts_with_big_odd=False,
    big_odd=[5, 7, 9],
):
    """Return a reason why the price is a bad red envelope price.

    If there is no reason to be found, raise `ReasonNotFound`.

    >>> get_why_bad(4000)
    'Contains 4.'
    >>> get_why_bad(5100)
    'Prefix is odd.'
    >>> get_why_bad(5000)
    'Prefix is odd.'
    >>> get_why_bad(5000, allow_prefix_is_odd=True)
    'Prefix could be changed to starts with the nearest even.'
    >>> get_why_bad(5000, allow_prefix_is_odd=True, big_odd=[9])
    Traceback (most recent call last):
    ...
    gong_xi_fa_cai.ReasonNotFound
    >>> get_why_bad(5120)
    'Needs to use change.'
    """
    if not allow_needs_to_use_change:
        if bad_signs.needs_to_use_change(price):
            return "Needs to use change."
    if not allow_contains_4:
        if bad_signs.contains_4(price):
            return "Contains 4."
    if not allow_contains_8:
        if bad_signs.contains_8(price):
            return "Contains 8."
    if not allow_prefix_is_odd:
        if bad_signs.prefix_is_odd(price, not_odd=not_odd):
            return "Prefix is odd."
    if not allow_prefix_is_too_long:
        if bad_signs.prefix_is_too_long(price, max_prefix_len=max_prefix_len):
            return "Prefix is too long."
    if not allow_prefix_starts_with_big_odd:
        if bad_signs.prefix_starts_with_big_odd(price, big_odd=big_odd):
            return "Prefix could be changed to starts with the nearest even."
    raise ReasonNotFound


def is_good(price, **kwargs):
    """Return whether the price is a good red envelope price.

    >>> is_good(1000)
    True
    >>> is_good(666)
    False
    >>> is_good(666, allow_needs_to_use_change=True, max_prefix_len=3)
    True
    >>> is_good(3000)
    False
    >>> is_good(3000, allow_prefix_is_odd=True)
    True
    >>> is_good(5000, allow_prefix_is_odd=True, big_odd=[9])
    True
    """
    try:
        get_why_bad(price, **kwargs)
    except ReasonNotFound:
        return True
    return False


def get_good_prices(max_price, min_price=1, **kwargs):
    """Return a list of good red envelope prices.

    >>> get_good_prices(max_price=6000)
    [100, 200, 600, 1000, 1200, 1600, 2000, 2200, 2600, 3200, 3600, 6000]
    >>> get_good_prices(min_price=3000, max_price=6000)
    [3200, 3600, 6000]
    >>> get_good_prices(min_price=3000, max_price=6000, not_odd=[1, 3])
    [3000, 3200, 3600, 6000]
    >>> get_good_prices(min_price=10000, max_price=15000)
    [10000, 12000]
    >>> get_good_prices(min_price=10000, max_price=15000, max_prefix_len=3)
    [10000, 10200, 10600, 11200, 11600, 12000, 12200, 12600, 13200, 13600]
    """
    good_prices = []
    for price in range(min_price, max_price + 1):
        if is_good(price, **kwargs):
            good_prices.append(price)
    return good_prices


def get_red_envelope(budget, max_error=0.1, **kwargs):
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
    >>> get_red_envelope(budget=66666)
    66000
    >>> get_red_envelope(budget=66666, max_prefix_len=3)
    66600
    """
    max_price = round(budget * (1 + max_error))
    good_prices = get_good_prices(max_price=max_price, **kwargs)
    red_envelope = get_nearest_number(good_prices, budget)
    return red_envelope
