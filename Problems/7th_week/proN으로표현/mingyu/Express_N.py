"""
Programmers. N으로 표현
url: https://programmers.co.kr/learn/courses/30/lessons/42895
writer: Mingyu
Language: Python3
Date: 2021.03.01
Status: , Runtime:  ms, Memory Usage:  KB
"""


def solution(N, number):
    # N으로 조합 가능한 모든 수의 집합. 초기값은 N을 아예 쓰지 않는 0, N만 들어있는 {N}으로 설정한다.
    comb_N = [0, {N}]

    # N == number라면 N 1개로 처리되는 것이므로 1을 return
    if N == number:
        return 1

    # 사용할 N의 개수를 2 이상 9 미만으로 설정. 위에서 N을 하나만 쓰는 경우를 이미 처리했기에 제한사항을 따르기 위해서는
    # 해당 for문에서는 9 이하가 아닌 9 미만으로 설정해야 한다.
    for i in range(2, 9):

        # N을 조합하여 만들 수 있는 수들의 집합, 중복 제거를 위해 set으로 설정
        comb_set = set()
        # 사칙연산을 사용하지 않은, 연속되게 붙인 숫자를
        serial_num = int(str(N)*i)
        comb_set.add(serial_num)

        # N이 사용되는 개수를 구하는 for문. 절반 이상 넘어가면 동일한 연산의 반복이므로 절반까지만 처리한다
        # 예시 : 절반 이전 = N1 * N2 ... 절반 이후 = N2 * N1 ...
        for i_half in range(1, i//2+1):
            # x에서 사용된 N의 개수와 y에서 사용된 N의 개수를 합하면 i개가 된다.
            for x in comb_N[i_half]:
                for y in comb_N[i-i_half]:

                    # 각 사칙연산을 수행
                    comb_set.add(x+y)
                    comb_set.add(x-y)
                    comb_set.add(y-x)
                    comb_set.add(x*y)
                    # 분모가 0이 아니어야 나눗셈을 할 수 있다.
                    if y != 0:
                        comb_set.add(x/y)
                    if x != 0:
                        comb_set.add(y/x)

            # 해당 N의 개수(i개)로 도출된 결과의 집합 안에 찾고자 하는 number가 있다면 i개를 사용했을 때 결과가 나온다는 뜻이다.
            if number in comb_set:
                return i

            # 해당 N의 개수로 도출된 결과의 집합을 comb_N에 넣는다
            comb_N.append(comb_set)

    # 범위를 전부 돌았음에도 값이 없다면 -1을 return
    return -1


print(solution(1, 1))

'''
def solution(N, number):
    comb_N = [0, {N}]

    if N == number:
        return 1

    for i in range(2, 9):
        comb_set = set()
        serial_num = int(str(N)*i)
        comb_set.add(serial_num)

        for i_half in range(1, i//2+1):
            for x in comb_N[i_half]:
                for y in comb_N[i-i_half]:
                    comb_set.add(x+y)
                    comb_set.add(x-y)
                    comb_set.add(y-x)
                    comb_set.add(x*y)
                    if y != 0:
                        comb_set.add(x/y)
                    if x != 0:
                        comb_set.add(y/x)

            if number in comb_set:
                return i

            comb_N.append(comb_set)

    return -1
'''
