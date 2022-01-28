def get_nearest_number(numbers, chosen):
    return min(numbers, key=lambda n: abs(n - chosen))


def get_prefix(price):
    prefix = str(price).rstrip("0")
    return prefix
