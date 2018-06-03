# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        lenr = len(rotateArray)
        if lenr == 0:
            return 0
        m = 0
        for i in range(lenr):
            if rotateArray[i] > rotateArray[i+1]:
                m = i+1
                break
        return rotateArray[m]
