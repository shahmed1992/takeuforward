"""Program to print name n times using recursion."""

class Solution:
    def __init__(self):
        pass
    def printName(self, n):
        if n > 0:
            self.printName(n-1)
            print("Hussain", end="\t")

solution = Solution()
solution.printName(5)
