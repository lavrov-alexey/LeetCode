'''15. 3 Sum (Medium)

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[1] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105'''


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
