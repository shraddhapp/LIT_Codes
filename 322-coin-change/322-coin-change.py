class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        min_coin = [amount+1]*(amount+1)
        min_coin [0] = 0
        print(min_coin)
        ''''
        for a in range(1, amount+1):
            for c in coins:
                if a-c >=0:
                    min_coin[a] = min(min_coin[a], 1+min_coin[a-c])
        return min_coin[amount] if min_coin[amount] != amount+1 else -1
    
        '''
        for i in range(1,(amount+1)):
            if i in coins:
                min_coin[i] = 1
            else:
                tempmin = amount+1
                for coin in coins:
                    k = i-coin
                    if(k>0):
                        tot = 1+min_coin[k]
                        #print("for",i,":rem=",k,"for coin",coin,"needed values of",k,":",min_coin[k])
                        if tot<tempmin:
                            tempmin=tot
                min_coin[i] = tempmin
                
      
        return min_coin[amount] if min_coin[amount] != amount+1 else -1