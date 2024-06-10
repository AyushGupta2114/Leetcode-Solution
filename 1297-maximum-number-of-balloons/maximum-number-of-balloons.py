class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text = text.lower()
        b_count = text.count('b')
        a_count = text.count('a')
        l_count = text.count('l') // 2
        o_count = text.count('o') // 2
        n_count = text.count('n')
        return min(b_count, a_count, l_count, o_count, n_count)
        