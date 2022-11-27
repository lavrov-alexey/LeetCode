if __name__ == '__main__':
    jewels = set(input())
    stones = input()
    # jewels = set('ab')
    # stones = 'aabbccd'
    stones = {stone: stones.count(stone) for stone in stones}
    # print(f'{jewels=}, {stones=}')
    cnt_jewels_in_stones = 0
    for stone, cnt_stone in stones.items():
        if stone in jewels:
            cnt_jewels_in_stones += cnt_stone
    print(cnt_jewels_in_stones)
