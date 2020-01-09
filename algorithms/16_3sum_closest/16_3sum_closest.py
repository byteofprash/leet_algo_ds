"""
Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def threeSum(nums):
    closest = None
    nums = sorted(nums)
    for i in range(len(nums)-2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right] + nums[i]
            if total < 0:
                left +=1
            elif total > 0:
                right -=1
            else:
                results.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left +=1
                while left < right and nums[right] == nums [right-1]:
                    right -=1
                left+=1
                right-=1
    return results


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0,0,0]))
print(threeSum([3,0,-2,-1,1,2]))
print(threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
