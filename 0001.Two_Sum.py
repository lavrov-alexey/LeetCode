'''1. Two Sum
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not
use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2)
time complexity?'''


class Solution(object):

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Return indices of the two numbers of an input array, that they add
        up to target. Complexity - O(n)
        Constraints: 2 <= len(nums) <= 1e4; -1e9 <= nums[i] <= 1e9;
        -1e9 <= target <= 1e9; only one valid answer exists.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict_diff_idx = dict()
        for idx_num, val_num in enumerate(nums):  # O(n)
            diff_to_target = target - val_num
            if not dict_diff_idx:  # if dict still empty
                dict_diff_idx[diff_to_target] = idx_num
                continue
            # if in dict already exists difference to target
            if val_num in dict_diff_idx:  # O(1)
                # returned two idx of two nums for target sum
                return [dict_diff_idx[val_num], idx_num]
            # save new element [different_to target]: idx for current num
            dict_diff_idx[diff_to_target] = idx_num

        # something wrong - return empty list
        return [0, 0]


if __name__ == '__main__':

    from time import time
    from random import randrange

    # tst_arr = [randrange(-10000, 10000) for _ in range(2000)]
    tst_arr = [2, 7, 11, 15]
    target = 9
    tst = Solution
    time_start = time()
    idx_num1, idx_num2 = tst.twoSum(tst, tst_arr, target)
    if idx_num1 or idx_num2:
        print(f'Sum of two elements (for {target=}): '
              f'nums[{idx_num1}]={tst_arr[idx_num1]} + '
              f'nums[{idx_num2}]={tst_arr[idx_num2]} = '
              f'{tst_arr[idx_num1] + tst_arr[idx_num2]}')
        print(f'Time for calculate: {(time() - time_start):f} sec.')
    else:
        print('Something wrong - two nums for sum target not finded!')
