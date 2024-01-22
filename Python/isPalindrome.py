class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i.lower() for i in s if i.isalnum()])
        if s == " " or s == "": return True

        mid = int(len(s)/2)

        first = ""
        second = ""
        if len(s[:mid]) > len(s[mid:]):
            first = s[:mid][:-1]
            second = s[mid:]
        elif len(s[:mid]) < len(s[mid:]):
            first = s[:mid]
            second = s[mid:][1:]
        else:
            first = s[:mid]
            second = s[mid:]

        for i, j in zip(first, second[::-1]):
            if i != j: return False
        
        return True