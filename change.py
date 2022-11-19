import re
from big2small import *
from small2big import *

def panduan(c):
    # result = []
# c = input()
# 判断是否是数字
    result =1
    #result =1 正确大写 result = 0 输入错误
    try:
        d = eval(str(c))
        result = 2 #小写
        return result
    except:
        # print("不是数字")
        CN_NUM = [
            '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', '拾', '零', '拾','佰','万','亿','兆',"元","整","仟"
        ]

        # 不是数字，判断大写是否有误
        t = 0
        for i in c:
            if i not in CN_NUM:
                # print("输入有误")
                result = 0
                t=1
                break
        if(t==0):
        # 判断大写逻辑是否正确
            small = mybig2small(c)
            print(small)
            big = mysmall2big(small)
            if big != c:
                # print("大写逻辑错误")
                result = 0


        return result