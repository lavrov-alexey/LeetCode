'''53. Maximum Subarray (Easy)

Given an integer array nums, find the contiguous subarray(containing at least
one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5, 4, -1, 7, 8]
Output: 23

Constraints:
1 <= nums.length <= 10**5, -10**4 <= nums[i] <= 10**4

Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.'''


class Solution(object):

    def maxSubArray(self, nums):
        """
        Finding the contiguous subarray (containing at least one number) which
        has the largest sum and returning its sum.
        A subarray is a contiguous part of an in-array.
        Simple - Brootforce variant - O(N2)
        Constraints: 1 <= nums.length <= 10**5, -10**4 <= nums[i] <= 10**4
        :type nums: List[int]
        :rtype: int
        """

        # strict constant
        MIN_ARR_CNT, MAX_ARR_CNT = 1, 100000
        MIN_ARR_VAL, MAX_ARR_VAL = -10000, 10000

        len_arr = len(nums)
        max_arr, min_arr = max(nums), min(nums)
        # print(f'Array {nums}, len {len_arr}, max/min items {max_arr}/{min_arr}')
        
        # check task constraints
        assert MIN_ARR_CNT <= len_arr <= MAX_ARR_CNT
        assert min_arr >= MIN_ARR_VAL and max_arr <= MAX_ARR_VAL

        max_sum, max_len = max_arr, 1
        # print(f'{max_sum=}, {max_len=}', end=', ')
        for len_sub_arr in range(2, len_arr + 1):
            start_idx = 0
            end_idx = start_idx + len_sub_arr
            # print(f'{start_idx=}, {end_idx=}')
            while end_idx <= len_arr:
                sum_sub_arr = sum(nums[start_idx:end_idx])
                # print(f'{sum_sub_arr=}, {nums[start_idx:end_idx]=}')
                if sum_sub_arr > max_sum:
                    max_sum = sum_sub_arr
                    max_len = len(nums[start_idx:end_idx])
                    # print(f'Find more sum! {max_sum=}, {max_len=}')
                start_idx += 1
                end_idx += 1
        return max_sum

    def maxSubArray_Kadane(self, nums):
        """
        Finding the contiguous subarray (containing at least one number) which
        has the largest sum and returning its sum.
        A subarray is a contiguous part of an in-array.
        Optimal - Kadanse's algoritm - O(N)
        Constraints: 1 <= nums.length <= 10**5, -10**4 <= nums[i] <= 10**4
        :type nums: List[int]
        :rtype: int
        """

        # strict constant
        MIN_ARR_CNT, MAX_ARR_CNT = 1, 100000
        MIN_ARR_VAL, MAX_ARR_VAL = -10000, 10000

        # check task constraints
        len_arr = len(nums)
        min_arr, max_arr = min(nums), max(nums)
        assert MIN_ARR_CNT <= len_arr <= MAX_ARR_CNT
        assert min_arr >= MIN_ARR_VAL and max_arr <= MAX_ARR_VAL

        # initialize starts values
        start_idx, end_idx = 0, 0  # start subarray index
        max_sum = nums[0]
        curr_sum = 0

        for idx in range(0, len(nums)):
            curr_sum = curr_sum + nums[idx]
            if curr_sum < 0:
                curr_sum = 0
                start_idx = idx + 1
            elif curr_sum > max_sum:
                max_sum = curr_sum
                end_idx = idx
        # print(f'{max_sum=}, {start_idx=}, {end_idx=}, {nums[start_idx:(end_idx+1)]}')

        return max_sum if max_sum >= max_arr else max_arr


if __name__ == '__main__':

    from time import time
    from random import randrange

    # tst_arr = [randrange(-10000, 10000) for _ in range(2000)]
    tst_arr = [-4, -7, -5, -1, -8]
    tst = Solution
    time_start = time()
    max_sub_array_sum = tst.maxSubArray(tst, tst_arr)
    print(f'Maximum sum of continuously subarray is {max_sub_array_sum}')
    print(f'Time for calculate: {(time() - time_start):f} sec.')

    time_start = time()
    max_sub_array_sum = tst.maxSubArray_Kadane(tst, tst_arr)
    print(f'Maximum sum of continuously subarray by Kadane algoritm is '
          f'{max_sub_array_sum}')
    print(f'Time for calculate: {(time() - time_start):f} sec.')
