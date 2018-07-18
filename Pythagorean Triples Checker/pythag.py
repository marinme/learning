import math
int_digits = [1,2,3,4,5,6,7,8,9,10]

def pythag(*source_nums):
    nums = list(source_nums)
    if len(nums) > 3:
        raise ValueError("Too many numbers")
    if not len(nums) == 3:
        for i in range(3 - len(nums)): # get remaining input
            nums.append(int(input("Input missing numbers, enter a numeric value: ")))
    if not set(int_digits).issuperset(set(nums)):
        raise ValueError("Invalid input")
    sorted_nums = sorted(nums)
    return (sorted_nums[0]**2 + sorted_nums[1]**2) == sorted_nums[2]**2