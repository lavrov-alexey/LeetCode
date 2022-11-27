# def lst_validation(in_lst):
#     MIN_EL, MAX_EL = 1, 100
#     MIN_CNT, MAX_CNT = 1, 100
#     try:
#         el_cnt, in_lst = int(in_lst[0]), list(map(int, in_lst[1:]))
#         assert MIN_CNT <= el_cnt <= MAX_CNT and el_cnt == len(in_lst)
#         for el in in_lst:
#             assert MIN_EL <= el <= MAX_EL
#     except (ValueError, AssertionError):
#         print(f'Входные данные {el_cnt=}, {in_lst=} не соответствуют условиям!')
#         exit(1)
#     return in_lst


if __name__ == '__main__':
    # lst1 = input().split()[1:]
    # lst2 = input().split()[1:]
    # lst3 = input().split()[1:]
    # print(f'{lst1=}')
    lst1 = list(map(int, input().split()[1:]))
    lst2 = list(map(int, input().split()[1:]))
    lst3 = list(map(int, input().split()[1:]))
    print(f'{lst1=}, {lst2=}, {lst3=}')



    # str1, str2, str3 = map(''.join, (lst1, lst2, lst3))
    # str1 = ''.join(lst1)
    # print(f'{str1=}')
    # print(f'{str1=}, {str2=}, {str3=}')

    # lst1 = list(map(int, input().split()))[1:]
    # lst2 = list(map(int, input().split()))[1:]
    # lst3 = list(map(int, input().split()))[1:]

    # if len(lst1) >= len(lst2) and len(lst1) >= len(lst3):
    #     str2_in_str1 = True if str2 in str1 else False
    #     str3_in_str1 = True if str3 in str1 else False
    # elif len(lst2) >= len(lst1) and len(lst2) >= len(lst3):
    #     str1_in_str2 = True if str1 in str2 else False
    #     str3_in_str2 = True if str3 in str2 else False
    # else:
    #     str1_in_str3 = True if str1 in str3 else False
    #     str2_in_str3 = True if str2 in str3 else False

    print(f'{str}')