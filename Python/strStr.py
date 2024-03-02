def strStr(haystack: str, needle: str) -> int:
    holder = haystack.split(needle)
    if len(holder) == 1:
        return -1
    return len(holder[0])


print(strStr("leetocode", "leeto"))