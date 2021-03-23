#This program is a sorting algorithm, that includes the "bubble" element. Essentially what it does, is it groups 2 numbers together, and you switch them if the number
    #on the left is bigger than the number on the right. 

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

        

