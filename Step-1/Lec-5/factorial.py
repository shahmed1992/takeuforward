"""Program to find factorial of n numbers"""


class Solution:

    def __init__(self):
        pass

    def factorial(self, n):
        if n == 0:
            return 1
        if n > 0:
            return n*self.factorial(n-1)


solution = Solution()
print(solution.factorial(5))
