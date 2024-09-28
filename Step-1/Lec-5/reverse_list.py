class Solution:
    def __init__(self):
        pass

    def reverseList(self, list1):
        print(f"Original List: {list1}")
        list1.reverse()
        print(f"Reversed list: {list1}")


solution = Solution()

# solution.reverseList([1, 2, 3, 4])

# To check reverse on a string

str1 = "abc"
str1 = str1[::-1]
print(str1)
