class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x != 0 or n > 0:
            return x**n
    
        return -1