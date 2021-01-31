"""
Baekjoon 9934. 완전 이진 트리
url: https://www.acmicpc.net/problem/9934
writer: Mingyu
Language: Python3
Date: 2021.01.25
Status: , Runtime:  ms, Memory Usage:  KB
"""
# 틀린 코드
# 왜 틀렸는지를 모르겠어서..

import sys

K = 3
building = [1, 6, 4, 3, 5, 2, 7]
# K = int(sys.stdin.readline())
# building = list(map(int, sys.stdin.readline().split()))
tree = [[] for _ in range(11)]

building = enumerate(building, start=1)

for index, building_num in building:
    if index % 2 == 1:
        tree[K-1].append(building_num)
        continue

    for x in range(1, 350, 2):
        if index == 2 * x:
            tree[K-2].append(building_num)
        elif index == 4 * x:
            tree[K-3].append(building_num)
        elif index == 8 * x:
            tree[K-4].append(building_num)
        elif index == 16 * x:
            tree[K-5].append(building_num)
        elif index == 32 * x:
            tree[K-6].append(building_num)
        elif index == 64 * x:
            tree[K-7].append(building_num)
        elif index == 128 * x:
            tree[K-8].append(building_num)
        elif index == 256 * x:
            tree[K-9].append(building_num)
        elif index == 512 * x:
            tree[K-10].append(building_num)

for i in tree:
    if i:
        for j in range(len(i) - 1):
            print(i[j], end= " ")
        print(i[len(i) -1])