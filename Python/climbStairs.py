class Solution:
    def climbStairs(self, n: int) -> int:
        ctr = 0
        fib = 1
        prev = 0
        cur = 1

        while ctr != n:
            cur = fib
            fib = prev + fib
            prev = cur
            ctr += 1

        return fib
