class Solution:

    # dict of conversion with roman and arabic tokens
    DICT_CONVERSION = {
        'M': 1000,
        'CM': 900,
        'DCCC': 800,
        'DCC': 700,
        'DC': 600,
        'D': 500,
        'CD': 400,
        'CCC': 300,
        'CC': 200,
        'C': 100,
        'XC': 90,
        'LXXX': 80,
        'LXX': 70,
        'LX': 60,
        'L': 50,
        'XL': 40,
        'XXX': 30,
        'XX': 20,
        'X': 10,
        'IX': 9,
        'VIII': 8,
        'VII': 7,
        'VI': 6,
        'V': 5,
        'IV': 4,
        'III': 3,
        'II': 2,
        'I': 1
    }

    def romanToInt(self, roman_num: str) -> int:
        """conversion a string with roman numbers to integer"""

        # easy prepare and validation input
        roman_num = roman_num.upper().strip()
        if not roman_num:
            raise ValueError(f'Roman number for conversion ({roman_num=}) '
                             f'is emty!')

        # rome number for conversion store to a class
        self.roman_num = roman_num

        # if case a Python lower ver.3.6 - make sort the dict of translation
        # by arabic nums (from higher to lower)
        tmp = sorted(self.DICT_CONVERSION.items(),
                     key=lambda x: x[1], reverse=True)
        self.DICT_CONVERSION = dict(tmp)
        del tmp

        result_int = 0  # for accumulate arabic value
        
        # iterate all pairs of romes and arabic values (tokens)
        # from dict of translation in descending order of arabic values
        for rome_token, arabic_token in self.DICT_CONVERSION.items():
            # while rome number starts with current rome token
            while roman_num.startswith(rome_token):
                result_int += arabic_token  # accumulate arabic value
                # cut from rome number current rome token
                roman_num = roman_num[len(rome_token):]
            if len(roman_num) == 0:  # if conversion is finished, return result
                self.arabic_num = result_int
                return self.arabic_num


if __name__ == '__main__':
    tst = Solution
    arabic_num = tst.romanToInt(tst, roman_num='MCMXCIV')
    print(f'{arabic_num=}')


# Очень элегантное решение:
# =========================
# # Initialize a dictionary to convert numerals to integer
# rMap = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000,
# }
# 
# 
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         # Initialize result with the last roman numeral
#         num = rMap[s[-1]]
# 
#         # Go from back to front starting from second last
#         for i in range(len(s) - 2, -1, -1):
#             # If current numeral's integer is greater than or equal to 
#             # that of the previous numeral then add it to the result
#             if rMap[s[i]] >= rMap[s[i + 1]]:
#                 num += rMap[s[i]]
# 
#             # Otherwise subtract it
#             else:
#                 num -= rMap[s[i]]
# 
#         # Final result will be our desired integer
#         return num