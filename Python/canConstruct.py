class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = {}
        ransomNote = list(ransomNote)
        for _i in ransomNote:
            if _i not in ransom: ransom[_i] = 0
            ransom[_i] += 1
        
        for _i in magazine:
            if _i in ransom:
                ransom[_i] -= 1
                if ransom[_i] == 0: ransom.pop(_i)
        
        if len(ransom) > 0: return False
        else: return True
