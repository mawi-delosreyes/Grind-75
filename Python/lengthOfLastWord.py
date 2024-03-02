def lengthOfLastWord(s: str) -> int:
    s = s.split(" ")

    for i in s[::-1]: 
        if i != "": return len(i)


lengthOfLastWord("   fly me   to   the moon  ")