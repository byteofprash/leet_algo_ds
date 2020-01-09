"""
1: Two sum
QUESTION:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums, target):
    """Returns the indices of the items when added equals to target

    :param nums: List of numbers
    :param target: adding up target
    :returns: TODO

    """
    for ind, num in enumerate(nums):
        num_to_find = target - num
        try:
            sec_ind = nums.index(num_to_find)
        except:
            continue
        if sec_ind == ind:
            continue
        else:
            return [ind, sec_ind]


print(twoSum([7, 11, 15, 2], target=9))
