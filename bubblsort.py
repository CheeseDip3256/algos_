def bubble_sort(nums):
    for i in range(len(nums)-1,-1,-1):
        for j in range(0,i):
            if nums[j] > nums[j+1]:
                swapval= nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = swapval
    return nums
    

sorted_numbers = bubble_sort([64,70,55,65,78]) 
print(sorted_numbers)

        

