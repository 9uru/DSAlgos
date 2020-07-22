def bubblesort(nums):
    if not nums or len(nums) <= 1:
        return nums

    end = len(nums) - 1
    
    while end > 0:
        for i in range(end):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        end = end - 1

    return nums

def selectionsort(nums):
    if not nums or len(nums) <= 1:
        return nums
    
    start = 0
    while start < len(nums) - 1:
        min_val = nums[start]
        min_pos = start
        for i in range(start + 1, len(nums)):
            if nums[i] < min_val:
                min_val = nums[i] 
                min_pos = i
        
        nums[start], nums[min_pos] = nums[min_pos], nums[start]

        start += 1
    
    return nums

def insert_val(nums, n):
    if n < nums[0]:
        nums.insert(0, n)
        return nums
    elif n > nums[-1]:
        nums.append(n)
        return nums
    else:
        return [nums[0]] + insert_val(nums[1:-1], n) + [nums[-1]]
    

nums = [2, 4, 3, 1, 7, 1, 8]
print(bubblesort(nums))
print(selectionsort(nums))

nums = [2, 3]
print(insert_val(nums, 1))
print(insert_val(nums, 4))
print(insert_val(nums, 1))
print(insert_val(nums, 4))
print(insert_val(nums, 2.5))