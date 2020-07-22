"""
Given an array of integers, return indices of the two numbers such that 
they add up to a specific target.

You may assume that each input would have exactly one solution, and you 
may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import time
# O(n^2)
def bruteforce(nums, target):
    for i, x in enumerate(nums):
        for j in range(i + 1, len(nums)):
            s =  x + nums[j]
            if s == target:
                return i, j
    return None


# O(n)
def hashtable(nums, target):
    comps = {}
    for i, x in enumerate(nums):
        val = target - x
        # print(val, comps)
        if x in comps:
            return comps[x], i
        comps[val] = i
    return None


if __name__ == '__main__':
    import random
    nums = random.choices(range(100), k=1000000)
    print(nums)
    target = 9
    start = time.time()
    print(bruteforce(nums, target))
    print(time.time() - start)
    start = time.time()
    print(hashtable(nums, target))
    print(time.time() - start)