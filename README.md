# gong-xi-fa-cai

Get the best red envelope.

# Run the doc tests

```
python3 tests.py -v
```

# Usages

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
>>> get_red_envelope(budget=66666, max_prefix_len=3)
66600
```

See `get_red_envelope` in `/gong_xi_fa_cai/__init__.py` for more details.
