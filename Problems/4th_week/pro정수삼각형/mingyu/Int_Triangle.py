"""
Programmers. 정수 삼각형
url: https://programmers.co.kr/learn/courses/30/lessons/43105
writer: Mingyu
Language: Python3
Date: 2021.02.04
Status: , Runtime:  ms, Memory Usage:  KB
"""

def solution(triangle):

    # 첫 번째 up은 루트 노드이자 하나밖에 없기 때문에 연산을 수행할 필요가 없다. 그러니 index는 1부터 시작
    for up in range(1, len(triangle)):

        # 다음 줄인 down은 항상 up보다 1이 크다. 그러니 길이는 up + 1.
        for down in range(up + 1):

            # 우선 가장 편하게 계산할 수 있는 부분은 모두 왼쪽 노드로 내려가는 것과 모두 오른쪽 노드로 내려가는 방법이 있다.
            # 첫 번째로 모두 왼쪽으로 내려가는 경우 (down의 인덱스가 0일 경우)
            if down == 0:
                # down은 계속 0이기 때문에 윗줄의 첫 번째 값을 더해 업데이트한다.
                triangle[up][down] += triangle[up-1][down]

            # 두 번째로 모두 오른쪽으로 내려가는 경우 (down의 인덱스가 up과 같을 경우)
            elif down == up:
                # 윗줄의 마지막 인덱스는 현재의 down에서 -1을 해주면 된다. 현재 줄이 윗 줄보다 한 칸 많기 때문.
                triangle[up][down] += triangle[up-1][down-1]

            # 좌우로 내려가는 경우룰 제외하고 나면 가운데에서 어떤 방식으로 내려갈 지 정해야 한다.
            # 밑 줄의 좌우 값 중 어떤 것을 현재 값과 더해야 더 큰 수가 되는지 판단하고, 더 큰수가 되는 쪽을 더하여 업데이트.
            else:
                triangle[up][down] += max(triangle[up - 1][down],
                                      triangle[up - 1][down - 1])

    # 맨 마지막 줄(triangle[-1])이 거쳐간 숫자들의 합을 담고 있으므로 이 중 가장 큰 값을 리턴한다.
    return max(triangle[-1])


''' 주석 없는 코드

def solution(triangle):

    for up in range(1, len(triangle)):
        for down in range(up + 1):
            if down == 0:
                triangle[up][down] += triangle[up-1][down]
            elif down == up:
                triangle[up][down] += triangle[up-1][down-1]
            else:
                triangle[up][down] += max(triangle[up - 1][down],
                                      triangle[up - 1][down - 1])

    return max(triangle[-1])
'''