"""
 Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 
"""


def maxArea(heights):
    """TODO: Docstring for maxArea.

    :param heights: TODO
    :returns: TODO

    """
    max_area = 0
    left = 0
    right = len(heights) - 1

    while left != right:
        possible_height = min(heights[left], heights[right])
        area = (right - left) * possible_height
        max_area = max(max_area, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1,2,3,2]))
