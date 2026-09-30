class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = {
            'b':0,
            'a':0,
            'l':0,
            'o':0,
            'n':0
        }
        for ch in text:
            if ch in counter:
                counter[ch] += 1
        return min(counter['b'],counter['a'],counter['l']//2,counter['o']//2, counter['n'])