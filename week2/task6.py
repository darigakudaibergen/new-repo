def all_eq(items):
    if not items:
        return []
        
    mx = max(len(s) for s in items)
    return [s + "_" * (mx - len(s)) for s in items]
