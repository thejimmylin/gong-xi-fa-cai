# gong-xi-fa-cai

Get the best red envelope.

# Run the doc tests

```bash
python3 tests.py -v
```

This allows you to run doc tests and produce results like this.
```bash
...
4 items passed all tests:
   5 tests in gong_xi_fa_cai.get_good_prices
   6 tests in gong_xi_fa_cai.get_red_envelope
   6 tests in gong_xi_fa_cai.get_why_bad
   6 tests in gong_xi_fa_cai.is_good
23 tests in 6 items.
23 passed and 0 failed.
Test passed.
```

# The basic usages

`gong_xi_fa_cai.get_red_envelope` returns a good red envelope price within your budget.
```python
>>> from gong_xi_fa_cai import get_red_envelope
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
```

# Other APIs

`gong_xi_fa_cai.get_good_prices` returns a good price list for a red envelope.
```python
>>> from gong_xi_fa_cai import get_good_prices
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
```

`gong_xi_fa_cai.is_good` returns whether the price is a good red envelope price.
```python
>>> from gong_xi_fa_cai import is_good
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
```

`gong_xi_fa_cai.get_why_bad` returns a reason why the price is a bad red envelope price.
```python
>>> from gong_xi_fa_cai import get_why_bad
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
```

See `/gong_xi_fa_cai/__init__.py` for more details.
