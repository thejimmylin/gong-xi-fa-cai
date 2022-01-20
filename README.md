# gong-xi-fa-cai

Get the best red envelope.

# Run the doc tests

```
python3 gong_xi_fa_cai.py -v
```

# Usages

```python
>>> from gong_xi_fa_cai import get_red_envelope
>>> get_red_envelope(budget=10000)
10000
>>> get_red_envelope(budget=9500)
10000
>>> get_red_envelope(budget=5000)
3600
>>> get_red_envelope(budget=5000, max_diff_rate=0.2)
6000
>>> get_red_envelope(budget=66666, max_prefix_len=3)
66600
```

See `get_red_envelope` in `gong_xi_fa_cai.py` for more details.
