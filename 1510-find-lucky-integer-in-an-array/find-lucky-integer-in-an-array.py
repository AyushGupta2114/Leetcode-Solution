from collections import Counter
import numpy as np
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        lucky = [num for num, count in freq.items() if num == count]
        return max(lucky) if lucky else -1  # -1 is often used when no lucky number exists
