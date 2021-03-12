"""
Baekjoon 15686. 치킨 배달
url: https://www.acmicpc.net/problem/15686
writer: Mingyu
Language: Python3
Date: 2021.03.03
Status: , Runtime:  ms, Memory Usage:  KB
"""
import sys
from itertools import combinations

read = sys.stdin.readline

# 입력 부분
n, m = map(int, read().split())
city = list()
for _ in range(n):
    city.append(list(map(int, read().split())))

# 집의 위치와 치킨집의 위치를 받는다
house_pos, chicken_pos = [], []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house_pos.append([i, j])
        elif city[i][j] == 2:
            chicken_pos.append([i, j])

# 최솟값을 구할 변수이므로 처음 비교될 수에 영향이 가지 않게 최댓값으로 설정
min_dis = sys.maxsize

# m개의 치킨집을 뽑았을 때 라는 제한사항이 있으므로
# 조합(combinations)를 통해 m개의 치킨집을 뽑아 for문을 돌린다.
for cp in combinations(chicken_pos, m):
    # 각 집에서 가장 가까운 치킨집까지의 거리의 합을 구할 변수
    sum_dis = 0

    # 집의 x, y좌표
    for hx, hy in house_pos:
        # min([abs(cx-hx) + abs(cy-hy) for cx, cy in cp]): 현재 집의 좌표(hx, hy)에서 갈 수 있는 치킨집의 좌표(cx, cy)를 list로 받아서
        # 이 중 가장 작은 값(min()), 즉 가장 가까운 치킨집까지의 거리를 sum_dis에 추가
        sum_dis += min([abs(cx-hx) + abs(cy-hy) for cx, cy in cp])

        # 지금까지 구한 치킨집까지의 거리의 합이 현재 저장되어 있는 최솟값보다 크다면 더 볼 필요가 없다.
        if min_dis <= sum_dis:
            break

    # 거리의 합이 현재 저장되어 있는 최솟값보다 작다면 min_dis를 업데이트
    if sum_dis < min_dis:
        min_dis = sum_dis

print(min_dis)


''' 주석 없는 코드

import sys
from itertools import combinations

read = sys.stdin.readline

n, m = map(int, read().split())

city = list()
for _ in range(n):
    city.append(list(map(int, read().split())))

house_pos, chicken_pos = [], []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house_pos.append([i, j])
        elif city[i][j] == 2:
            chicken_pos.append([i, j])

min_dis = sys.maxsize

for cp in combinations(chicken_pos, m):
    sum_dis = 0
    for hx, hy in house_pos:
        sum_dis += min([abs(cx-hx) + abs(cy-hy) for cx, cy in cp])
        if min_dis <= sum_dis:
            break

    if sum_dis < min_dis:
        min_dis = sum_dis

print(min_dis)
'''


''' 왜 안됐을까?
distances = list()
for cx, cy in chicken_pos:
    min_dis = sys.maxsize
    sum_dis = 0
    for hx, hy in house_pos:
        sum_dis += abs(cx - hx) + abs(cy - hy)
        if abs(cx - hx) + abs(cy - hy) < min_dis:
            min_dis = abs(cx - hx) + abs(cy - hy)

    distances.append([min_dis, sum_dis, cx, cy])

distances = sorted(distances)[:m]

answer = []
for hx, hy in house_pos:
    tmp = []
    for _, _, cx, cy in distances:
        tmp.append(abs(cx-hx) + abs(cy-hy))
    answer.append(min(tmp))
'''
