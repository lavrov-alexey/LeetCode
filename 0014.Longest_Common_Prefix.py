'''0014. Longest Common Prefix (Easy)
Write a function to find the longest common prefix string amongst an array
of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.'''


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # find min lenght of str in strs
        min_len_str = len(strs[0])
        for curr_str in strs:
            if len(curr_str) < min_len_str:
                min_len_str = len(curr_str)
        if min_len_str == 0:
            return ""

        common_prefix = ""
        for idx in range(0, min_len_str):
            curr_char = strs[0][idx]  # get idx's char of first str
            is_not_all_eqw_char = False
            for curr_str in strs:
                if curr_str[idx] != curr_char:
                    is_not_all_eqw_char = True
                    break
                # print(f'{curr_str=}, {idx=}, {curr_char=}, {curr_str[idx]=}')
            if is_not_all_eqw_char:  # current char is'nt part of common prefix
                return common_prefix
            common_prefix += curr_char
        return common_prefix


if __name__ == '__main__':
    words_array = ["flower", "flow", "flight"]  # first test case
    tst = Solution
    res = tst.longestCommonPrefix(tst, words_array)
    print(res)
