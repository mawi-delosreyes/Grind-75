def plusOne(digits: list[int]) -> list[int]:

    carry = True
    for i in range(len(digits)-1, -1, -1):
        if not carry: break

        if digits[i] + 1 > 9: 
            digits[i] = 0
        else: 
            digits[i] += 1
            carry = False
        
    if carry == True: 
        digits[0] = 0
        digits.insert(0, 1)

    return digits        
            



print(plusOne([9]))