"""Program to find sum of first n numbers"""


class Solution:
    def __init__(self):
        pass

    def sum_n_numbers(self, n):
        if n == 0:
            return 0
        if n > 0:
            return n + self.sum_n_numbers(n-1)


solution = Solution()
print(solution.sum_n_numbers(54))
