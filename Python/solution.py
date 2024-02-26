
def solution(N):
    
    max_num = 0
    if N < 0: 
        max_num = N
    
    N = str(N)

    for i in range(len(N)):
        if N[i] == '5':
            if max_num < int(N[:i] + N[i+1:]):
                max_num = int(N[:i] + N[i+1:])


    return max_num

            


print(solution(5859))