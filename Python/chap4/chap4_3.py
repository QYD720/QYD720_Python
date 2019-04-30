# Author : QYD720 
# Time : 2019/4/10

# 4.3 创建数值列表
# 需求: 生存打印1-20内偶数；
#       转换这些偶数为列表性质集合；
#       转换此偶数列表为偶数立方列表；
#       计算3次方列表的最大最小值 合计
# 分析：/rang(开始，结束，步长)/代码实现输出，for X in XX实现循环打印偶数；
#       转换数据为列表性质，可以直接list();或者空列表+列表.append(循环导入)；
#       遍历输出，立方数**3处理后,装进空列表
#       min max sum()函数

for odd in range(2, 21, 2):
    print(odd)  # 遍历输出

print("\n")

# 空袋子装进去
list1 = []
for odd in range(2, 21, 2):
    list1.append(odd)
print(list1)

# list化
list2 = list(range(2, 21, 2))
print(list2)

T3 = []  # 造一个空箱子
for odd in list2:  # 旧箱子里一个一个拿出来
    odd1 = odd**3  # 化个妆
    T3.append(odd1)   # 装进新箱子
print(T3)


X = [1, 2, 3, 4, 5]
sum1 = sum(list2)
print(sum1)
print(min(X))
print(max(X))

