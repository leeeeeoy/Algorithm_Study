"""
Programmers. 문자열 압축
url: https://programmers.co.kr/learn/courses/30/lessons/60057
writer: Mingyu
Language: Python3
Date: 2021.02.01
Status: , Runtime:  ms, Memory Usage:  KB
"""


def solution(s):
    # answer변수를 사용하여 min 비교를 할 것이다
    # 첫 min 비교에서 변수로 작용하면 안되므로 s의 최대 길이 1000보다 1을 크게 설정
    answer = 1001

    # 문자열의 반복을 보는 것이기 때문에 절반까지만 검사하면 된다.
    for cut in range(1, len(s) // 2 + 1):
        # 잘라낸 문자열들을 추가할 변수
        res = ""
        
        # 반복되는 문자열의 수. 처음이 1인 이유는 x * 1 = x이기 때문이다.
        cnt = 1

        # 비교의 기준이 되는 변수. cut만큼 잘라내어 비교 단위로 사용한다.
        tmp = s[:cut]

        # 잘라낸 위치의 마지막부터 s의 길이만큼(cut부터 시작하므로 +cut을 해주어야 길이가 맞게 나온다) cut단위로 진행
        for i in range(cut, len(s) + cut, cut):

            # s[i]부터 cut만큼의 길이가 비교 기준인 tmp와 같다면
            if tmp == s[i: i+cut]:
                # 동일한 문자열이 있는 것이므로 반복 문자열의 수를 +1 한다.
                cnt += 1
            
            # 더 이상 동일한 문자열이 없을 경우
            else:
                # cnt가 1보다 크다면 동일한 문자열이 더 있다는 뜻이다.
                if cnt > 1:
                    # 동일한 문자열은 숫자로 치환하여 출력한다.
                    # cnt를 str형태로 바꾸어 "숫자+문자열"의 형태로 res에 추가
                    res += str(cnt)+tmp
                
                # 동일한 문자열이 없다면
                else:
                    # tmp를 그대로 res에 넣어준다
                    res += tmp
                
                # cut의 길이는 동일한 상태로 cut의 시작점을 i번째로 바꾼다.
                tmp = s[i:i+cut]
                # cnt 또한 1로 초기화
                cnt =1
        
        # answer과 res의 길이를 비교하여 더 짧은 쪽을 answer로 업데이트
        answer = min(answer, len(res))
    
    # 맨 처음에 answer를 최대값으로 초기화하였다. 혹시라도 위의 for문을 돌았음에도 차이가 없을 수 있기 때문에
    # answer과 s의 길이를 비교하여 변한 것이 없다면 s의 길이를 리턴한다.
    return min(answer, len(s))


''' 주석 없는 코드

def solution(s):
    answer = 1001

    for cut in range(1, len(s) // 2 + 1):
        res = ""       
        cnt = 1
        tmp = s[:cut]

        for i in range(cut, len(s) + cut, cut):

            if tmp == s[i: i+cut]:
                cnt += 1     

            else:
                if cnt > 1:
                    res += str(cnt)+tmp  
                                  
                else:
                    res += tmp
                
                tmp = s[i:i+cut]
                cnt =1
        
        answer = min(answer, len(res))
    
    return min(answer, len(s))
'''