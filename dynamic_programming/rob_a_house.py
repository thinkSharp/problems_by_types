"""
robbing a house can be performed if not two adjacent houses were robbed. If 
1 identify recurrance relation:
   in order to maximize the outcome, either you will steal next house or skip one + current house
2. base cases
    if zero house => 0
    if one house => house[0]
3. Create recursive function:
    def rob(houses: list[int]) -> int:
        if not houses:
            return 0
        total_rob = 0

        def rob_helper(house_no):
            if house_no == 0:
                return 0
            if house_no == 1:
                return houses[0]
            
            return max(rob_helper(house_no - 1), rob_helper(house_no - 2) + houses[house_no - 1])
    return rob(len(houses))

4. Memorize the recursive function 
    def rob(houses: list[int]) -> int:
        if not houses:
            return 0
        total_rob = 0
        memo = {}
        def rob_helper(house_no):
            if house_no == 0:
                return 0
            if house_no == 1:
                return houses[0]
            
            if house_no in memo:
                return memo[house_no]
            memo[house_no] = max(rob_helper(house_no - 1), rob_helper(house_no - 2) + houses[house_no - 1])
            return memo[house_no]
    return rob(len(houses))

5. Convert top down (recursive) to Bottom Up (loop)
    def rob(houses: list[int]) -> int:
        dp = [0] * len(houses) + 1
        dp[1] = houses[0]
        for i in range(2, len(houses) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + houses[i - 1])
        
        return dp[len(houses)]
6. Optimization: since we only need to track two values, keeping entire array is overkill
    def rob(houses: list[int]) -> int:
        prev, curr = 0, houses[0]
        for i in range(2, len(houses) + 1):
            take = prev + houses[i - 1]
            skip = curr
            prev, curr = curr, max(take, skip)
        return curr
        
"""