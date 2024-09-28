class Solution:
    def __init__(self):
        pass
    def checkPrime(self, nums):
        for num in nums:
            count = 0
            for i in range(2, num-1):
                if num % i == 0:
                    count += 1
                    # print(f"{count=}")
            if count > 0:
                print(f"{num} Not a prime number")
            else:
                print(f"{num} is a prime number")


solution = Solution()
solution.checkPrime([92, 85, 76, 91, 11])
