'''
	Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0


'''

import bisect

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums, target)


'''
The desired insertion position is easily found with the bisect.bisect_left function. Although this is a trivial application of this function, more difficult leetcode problems leverage this function, so it is worthwhile to know about.

https://docs.python.org/2.7/library/bisect.html?highlight=bisect#bisect.bisect_left
'''


'''
   Another Solution - 

   class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            for i,j in enumerate(nums):
                if j>target:
                    return i
            return i+1

'''