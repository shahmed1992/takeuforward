"""Program to print 1-n numbers using recursion"""


class Solution:
    def __init__(self):
        pass

    def print_numbers(self, n):
        if n > 0:
            self.print_numbers(n - 1)
            print(n)


solution = Solution()
solution.print_numbers(5)
