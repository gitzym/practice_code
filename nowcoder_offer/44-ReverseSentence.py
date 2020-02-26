# -*- coding:utf-8 -*-
# 翻转句子
class Solution:
    def ReverseSentence(self, s):
        # write code here
        s_l = s.split(" ")
        mid = int((len(s_l) - 1) / 2)
        for i in range(mid + 1):
            temp = s_l[-(i + 1)]
            s_l[-(i + 1)] = s_l[i]
            s_l[i] = temp
            print(s_l)

        return " ".join(s_l)

class Solution_:
    '''
    这是python的slice语法, 可以理解为[begin, end, step], step为步长。
    当指定step而不指定begin和end时，会根据step的正负来正向或反向地遍历所有元素。
    step为负，则从右到左切片。
    '''
    def ReverseSentence(self, s):
        return "".join(s.split()[::-1]) if s.strip() != "" else s

class Solution_2reverse:
    '''
    【两次翻转】先翻转整个句子，再根据空格确定单词，翻转单词
    '''
    def ReverseSentence(self, s):
        pass

'''
另一种思路：
1 
从前往后一直读取，遇到空格之后就把之前读取到的压到结果的前面并添加上空格。最后当循环结束，如果那个用来读取的字符串不为空，
那么就再把它压到结果前，这次就不用再结果的最前面加空格了，这应该就是思路吧，开始我也这么想不过觉得太朴素了，不够酷炫，后来想了想。
这个的时间复杂度会低一点，不过额外多用点内存。
2 
用栈

'''

# s = Solution()
# res = s.ReverseSentence("I am a student.")
# print(res)


ss = list("I am a student.")
print(ss[3:])

ss[3],ss[7] = ss[7], ss[3]
print(ss)

