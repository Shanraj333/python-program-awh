nums = [2, 34, 67, 8, 25, 89,90]
for i in range(0,len(nums)-1):
    if nums[i]<nums[i+1]:
        large=nums[i+1]
print(large)