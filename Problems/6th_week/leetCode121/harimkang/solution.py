"""
LeetCode 121. Best Time to Buy and Sell Stock
url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
writer: Harim Kang
Language: Python3
Date: 2021.02.27
Status: Success, Runtime: 68 ms, Memory Usage: 15.1 MB
"""
import sys


class Solution:
    def maxProfit(self, prices):
        answer = 0
        min_price = sys.maxsize

        for p in prices:
            min_price = min(p, min_price)
            answer = max(answer, p - min_price)

        return answer


if __name__ == "__main__":
    input_1 = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(input_1))
    input_2 = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(input_2))
    # input_3 = [1, 0]
    # print(Solution().maxProfit(input_3))
