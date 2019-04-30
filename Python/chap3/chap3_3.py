# Author : QYD720
# Time : 2019/4/6

#  3.3 组织列表-永久性排序，临时性排序，获取列表长度，倒叙打印列表
# 需求：输出原始排名，临时字母排列打印，最后输出永久性倒叙字母原始排序;确定列表长度
# 分析：print输出，/sorted()/临时排序，打印输出；/列表名.sort（reverse=ture）/永久性倒字母排序；/len（）/函数计算列表长度
Richmen = ["jack Ma", "yanhong LI", "ajianling WAng", "sicong WANg"]
print(Richmen)
print("\n")

temp = sorted(Richmen)
print(temp)
print("\n")

Richmen.sort(reverse=True)
print(Richmen)
print("\n")

lg = len(Richmen)
print("列表长度是"+str(lg))
