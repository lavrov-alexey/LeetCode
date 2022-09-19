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
-10**5 <= nums[i] <= 10**5'''

import itertools as it
import random as rnd

class Solution(object):
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        MIN_LEN_ARRAY, MAX_LEN_ARRAY = 3, 10**5
        MIN_VAL_EL, MAX_VAL_EL = -10**5, 10**5
        assert MIN_LEN_ARRAY <= len(nums) <= MAX_LEN_ARRAY + 1
        assert min(nums) >= MIN_VAL_EL and max(nums) <= MAX_VAL_EL

        uniq_tripl_idx = it.combinations((idx for idx in range(len(nums))), 3)
        uniq_tripl_val = {tuple(sorted([nums[idx1], nums[idx2], nums[idx3]]))
                          for idx1, idx2, idx3 in uniq_tripl_idx
                          if nums[idx1] + nums[idx2] + nums[idx3] == 0}
        res = [list(curr_tripl) for curr_tripl in uniq_tripl_val]
        return res


if __name__ == '__main__':
    # nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 1, 1]
    # nums = [0, 0, 0]
    nums = [rnd.randint(-100000, 100001) for _ in range(200)]
    print(f'{len(nums)=}, {nums=}')

    tst = Solution
    res = tst.three_sum(tst, nums)
    print(f'{len(res)=}, {res=}')
