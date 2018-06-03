# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        fb = [1,1]
        if n == 0:
            return 0
        if n>0 and n <= 2:
            return fb[n-1]
        for i in range(2, n):
            fb.append(fb[i-1]+fb[i-2])
        return fb[-1]
