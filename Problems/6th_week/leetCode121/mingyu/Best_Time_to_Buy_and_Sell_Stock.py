<<<<<<< HEAD
"""
LeetCode 121. 주식거래하기 딱 좋은 날씨네
url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
writer: Mingyu
Language: Python3
Date: 2021.02.24
Status: , Runtime:  ms, Memory Usage:  KB
"""

from heapq import heappush

prices = [7, 1, 5, 3, 6, 4]

def maxProfit(prices):

    # prices의 길이가 1이라면 계산이 불가능하다. 그러므로 0을 리턴
    if len(prices) < 2:
        return 0

    # 최소값을 갱신할 heapq 생성
    min_price = []
    # 현재까지 도출된 최대 이익
    profit = 0

    # for문을 사용하여 오늘의 주식 가격을 계속 돌면서
    for price in prices:
        # 오늘의 주식 가격을 min_price에 heapq로 저장
        # heapq의 작동 방식에 따라 가장 작은 값이 min_price[0]에 업데이트된다.
        heappush(min_price, price)

        # 오늘의 주식 가격 - 이전 주식 가격 중 가장 작은 값이 현재까지 도출된 최대 이익보다 크다면
        if price - min_price[0]> profit:
            # 해당 값을 최대 이익으로 업데이트
            profit = price - min_price[0]

    # 최대 이익을 return
    return profit


''' 주석 없는 코드

def maxProfit(prices):

    if len(prices) < 2:
        return 0

    min_price = []
    profit = 0
    for price in prices:
        heappush(min_price, price)

        if price - min_price[0]> profit:
            profit = price - min_price[0]
        print(price, min_price[0], profit)

    return profit
'''
   


print(maxProfit(prices))
=======
"""
LeetCode 121. 주식거래하기 딱 좋은 날씨네
url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
writer: Mingyu
Language: Python3
Date: 2021.02.24
Status: , Runtime:  ms, Memory Usage:  KB
"""

from heapq import heappush

prices = [7, 1, 5, 3, 6, 4]

def maxProfit(prices):

    # prices의 길이가 1이라면 계산이 불가능하다. 그러므로 0을 리턴
    if len(prices) < 2:
        return 0

    # 최소값을 갱신할 heapq 생성
    min_price = []
    # 현재까지 도출된 최대 이익
    profit = 0

    # for문을 사용하여 오늘의 주식 가격을 계속 돌면서
    for price in prices:
        # 오늘의 주식 가격을 min_price에 heapq로 저장
        # heapq의 작동 방식에 따라 가장 작은 값이 min_price[0]에 업데이트된다.
        heappush(min_price, price)

        # 오늘의 주식 가격 - 이전 주식 가격 중 가장 작은 값이 현재까지 도출된 최대 이익보다 크다면
        if price - min_price[0]> profit:
            # 해당 값을 최대 이익으로 업데이트
            profit = price - min_price[0]

    # 최대 이익을 return
    return profit


''' 주석 없는 코드

def maxProfit(prices):

    if len(prices) < 2:
        return 0

    min_price = []
    profit = 0
    for price in prices:
        heappush(min_price, price)

        if price - min_price[0]> profit:
            profit = price - min_price[0]
        print(price, min_price[0], profit)

    return profit
'''
   


print(maxProfit(prices))
>>>>>>> e9cb03456e11cb14bf5d8fb8b196449990655e38
