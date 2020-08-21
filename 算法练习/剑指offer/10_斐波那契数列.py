'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''
class Solution:
    def Fibonacci(self, n):
        if n <= 1:
            return n
        return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
'''
解法2
class Solution:
    def Fibonacci(self, n):
        res=[0, 1, 1]
        for _ in range(n):
            res[0], res[1], res[2] = res[1], res[2], res[1] + res[2]
        return res[0] if n > 2 else res[n]


解法3
class Solution:
    def Fibonacci(self, n):
        a, b = 1, 0
        for _ in range(n):
            a, b = a+b, a
        return b

'''