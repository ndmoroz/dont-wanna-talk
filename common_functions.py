def are_equal_dicts(dict1, dict2, *ignore_keys):
    d1_filtered = dict(
        (k, v) for k, v in dict1.items() if k not in ignore_keys)
    d2_filtered = dict(
        (k, v) for k, v in dict2.items() if k not in ignore_keys)
    return d1_filtered == d2_filtered
