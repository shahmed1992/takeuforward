"""Program to find Divisors of all numbers"""

class Solution:
    def __init__(self):
        pass


    def find_divisors(self, nums:list):
        res = {}
        for num in nums:
            temp = []
            for i in range(2, num):
                if num%i == 0:
                    temp.append(i)
            res[num] = temp

        return res

solution = Solution()
output = solution.find_divisors([34, 45, 54])
print(output)
