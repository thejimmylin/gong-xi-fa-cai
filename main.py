# good_numbers = [2, 6, 8]
# good_numbers += [10, 12, 16, 18]
# good_numbers += [20, 22, 26, 28]
# good_numbers += [32, 36]
# good_numbers += [60, 66, 68]
# good_numbers += [80, 86, 88]


# def get_red_envelope():

for n in range(1, 10000):
    if n % 100 != 0:
        continue
    prefix = str(n).rstrip("0")
    if int(prefix) % 2 != 0:
        continue
    if "4" in str(prefix):
        continue
    print(n)
