class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
        d= Counter(power)
        for i in d:
            d[i] = i * d[i]
        power.sort()
        dp = [0]*len(set(power))
        dp[0] = [d[power[0]] , 0]
        power = sorted(set(power))
        currentMax = 0
        for i in range(1, len(power)):
            take = d[power[i]]
            leave = 0
            if power[i]>=power[i-1] + 3:
                take = max(dp[i-1][0] , dp[i-1][1]) + d[power[i]]
            else:
                t = i - 1
                while t >= 0 and power[t] + 3 > power[i]:
                    t -= 1
                if t >=0:
                    take = max(dp[t][0] , dp[t][1]) + d[power[i]]
            leave = max(dp[i-1])
            dp[i] = [take, leave]

        return max(dp[len(power) - 1])


