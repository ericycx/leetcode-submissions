class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        H = [0] + [INF] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i and H[i - coin] + 1 < H[i]:
                    H[i] = H[i - coin] + 1
        return H[amount] if H[amount] <= amount else -1