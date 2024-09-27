""" Program to find if a number is a Armstrong number or not!! """
sum_value = 0
nums = [153, 372]
for num in nums:
    num_digits = len(str(num))
    temp = num
    while temp:
        sum_value += (temp % 10)**num_digits
        temp//=10
    if sum_value == num:
        print(f"{num} is a Armstrong Number")
    else:
        print(f"{num} is Not a Armstrong Number")

