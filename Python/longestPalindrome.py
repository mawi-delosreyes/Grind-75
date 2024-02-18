def longestPalindrome(s: str) -> int:
    holder = {}
    even = 0
    odd = 0
    with_odd = False

    if len(s) == 1: return 1

    for i in s:
        if i not in holder: holder[i] = 1
        else: holder[i] += 1

    for i in holder:
        if holder[i] % 2 == 0: even += holder[i]
        else: 
            with_odd = True
            odd += (holder[i] - 1)


    total = odd + even

    if odd % 2 == 0 and with_odd: total += 1
    return total
