class Solution:
    def coinChange(self, coins, amount):
        #dp solution
        dp_array=[amount+1]*(amount+1)
        dp_array[0]=0
        print(dp_array)
        # for i in range(len(coins)):
        #   # dp_array[i]=-1
        #   dp_array[coins[i]]=1
        # print(dp_array)
        # return

        for cur_amount in range(1, amount+1):
            for coin in reversed(coins):      
                print(cur_amount, coin)
                print(dp_array)
                if cur_amount-coin>=0:
                    print("inside if")
                    dp_array[cur_amount] =min(dp_array[cur_amount], dp_array[cur_amount-coin]+1)
        return dp_array[amount]
        


        #Backtracking 1
        # gn_coins=float("inf")
        # return self.coinB1(coins, amount, gn_coins)


        #backtracking 2
    #     global_min=amount+1
    #     num_of_coins=0
    #     return self.coinB2(coins, amount,global_min, num_of_coins)

    # def coinB1(self, coins, amount, gn_coins):
    #     if amount==0:
    #         return 1
    #     if amount<0:
    #         return 0
    #     if len(coins)<=0 and amount>0:
    #         return 0
    #     n_coins= self.coinB1(coins[:-1], amount, gn_coins)+self.coinB1(coins[:], amount-coins[len(coins)-1], gn_coins)

    #     gn_coins= min(n_coins, gn_coins)
    #     return gn_coins

    # def coinB2(self, coins, amount, global_min, num_of_coins):
    #     print(amount, global_min, num_of_coins)
    #     if amount<0:
    #         return 0
    #     if amount ==0:
    #         global_min=int(min(global_min, num_of_coins))
    #         return global_min

    #     for coin in coins:
    #         ret=self.coinB2(coins, amount-coin, global_min, num_of_coins+1)
    #         if ret!=0:
    #             global_min=min(ret, global_min)

    #     return global_min






if __name__=="__main__":
    s=Solution()
    print(s.coinChange([1, 2, 5], 11))