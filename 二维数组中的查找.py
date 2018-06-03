# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m = 0
        for i in range(len(array)):
            if target in array[i]:
                m += 1
            else:
                continue
        return m != 0
