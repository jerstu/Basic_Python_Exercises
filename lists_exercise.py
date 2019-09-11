nums = [1, 2, 3, 250, 33, 12, 4, 99, 26, 44, 55, 66, 60]
maximum = nums[0]
for num in nums:
    if num > maximum:
        maximum = num
print(maximum)
