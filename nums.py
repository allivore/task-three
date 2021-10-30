def find_missing_nums(nums=list):
    n = nums[-1]
    full = [x for x in range(1, n+1)]
    missing = []
    for value in full:
        if value in nums:
            continue
        else:
            missing.append(value)

    return missing
