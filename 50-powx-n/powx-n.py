class Solution:
    def myPow(self, x, n):
        def power(x, n):
            if n == 0:
                return 1
            half = power(x, n // 2)
            if n % 2:
                return half * half * x
            return half * half

        return power(x, n) if n >= 0 else 1 / power(x, -n)