def sort(nums):

    for i in range(9):
        minpos = i
        for j in range(i,10):
            if nums[j] < nums[minpos]:
                minpos = j


        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print('Array:', nums)


nums = [62, 28, 41, 15, 12, 89, 78, 51, 35, 83]
print('Array:', nums)
sort(nums)

print('Array:', nums)