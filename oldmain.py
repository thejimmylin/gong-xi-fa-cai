def get_prefixes(
    first=("", "1", "2", "3", "6", "8"),
    second=("0", "2", "6", "8"),
):
    prefixes = []
    for first_char in first:
        for second_char in second:
            prefix = first_char + second_char
            prefixes.append(prefix)
    prefixes.remove("0")
    return prefixes


def get_prices(
    max_price,
    first=("", "1", "2", "3", "6", "8"),
    second=("0", "2", "6", "8"),
):
    prices = []
    prefixes = get_prefixes(first=first, second=second)
    ratio = 100
    while True:
        new_prices = [int(prefix) * ratio for prefix in prefixes]
        min_price = min(new_prices)
        if min_price > max_price:
            prices = [price for price in prices if price <= max_price]
            prices = sorted(list(set(prices)))
            return prices
        prices.extend(new_prices)
        ratio = ratio * 10
