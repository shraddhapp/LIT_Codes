class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        buy,sell = 0,1
        
        while(sell < len(prices)):
            #print('buy pos: {}, sell pos: {} curr buy: {}, curr sell: {}'.format(buy, sell, prices[buy], prices[sell]))
            
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                sell+=1
                if profit > max_p:
                    max_p = profit
                #print("calculated profit",profit,'max_p is', max_p)
            else:
                #print("going ahead")
                buy = sell
                sell +=1
        
        return max_p