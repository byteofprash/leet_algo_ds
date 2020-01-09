"""
4_median_two_sorted_arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


def findMedianSortedArrays(nums1, nums2):
    """Find the median or two arrays

    :param nums1: TODO
    :param nums2: TODO
    :returns: TODO

    """
    combined_list = []
    combined_list = nums1 + nums2
    combined_list.sort()
    num_len = len(combined_list)
    print(combined_list)
    if num_len % 2 == 0:
        return (combined_list[(num_len // 2) - 1] + combined_list[(num_len // 2)]) / 2.0
    return combined_list[num_len // 2]


