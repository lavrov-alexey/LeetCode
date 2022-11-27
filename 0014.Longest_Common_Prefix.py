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
        min_len_str = 0
        for el in strs:
            if len(el) > min_len_str:
                min_len_str = len(el)

        for idx in range(0, min_len_str):
            

        return res


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]

    tst = Solution
    res = tst.longestCommonPrefix(strs)
    print(res)