# Author : QYD720 
# Time : 2019/4/18

# 5.2 if语句条件测试
# 需求：在国家列表里，如果是中国，则输出大写，否则 输出小写。
# 方法：利用“if XX ==:  else”语法判断

country = ["China", "USA", "Canada", "UK", "France",  "Japan", "German"]
for co in country:
    if co.lower() == 'china':
        print(co.upper())
    else:print(co.lower())

if "China" in country:
    print("zai!")

CN = "China"
if CN == "china":
    print("找到了！")
else:print("no fond")
# 检查是否相等


lighting = "OFF"
if lighting != "ON":
    print("请开灯！")
# 检查是否不等


'''


这是一个

'''
