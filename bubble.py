def sort(nums):

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                print('Array:', nums)


nums = [62, 28, 41, 15, 12, 89, 78, 51, 35, 83]
print('Array:', nums)
sort(nums)

print('Array:', nums)