class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        result = float("inf")
        a = []
        for i in timePoints:
            hours = i.split(":")[0]
            minutes = i.split(":")[1]
            hours = int(hours)
            hours = hours * 60
            minutes = int(minutes)
            minutes = minutes + hours
            a.append(minutes)

        a.sort()

        for i in range(1, len(a)):
            diff = a[i] - a[i-1]
            result = min(result, diff)
        
        final = 1440 - a[-1] + a[0]

        return min(result, final)


