def containsDuplicate(nums: list[int]) -> bool:

    num_len = len(nums)
    check_dup = len(set(nums))

    if num_len != check_dup: return True
    return False




