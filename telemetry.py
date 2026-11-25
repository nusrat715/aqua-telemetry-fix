def depth_status(age_s):
    if age_s is None:
        return "NO DATA"
    if age_s < 2:
        return "LIVE"
    return "STALE"
