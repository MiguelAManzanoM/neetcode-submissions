class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0

        minSeen = prices[0]
        maxDiff = 0

        for i in range(1, len(prices)):
            currentVal = prices[i]

            if currentVal > minSeen:
                currentDiff = currentVal - minSeen
                maxDiff = max(maxDiff, currentDiff)

            if minSeen > currentVal:
                minSeen = currentVal
        
        return maxDiff
