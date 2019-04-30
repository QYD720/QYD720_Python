#Author : QYD720 
#Time : 2019/4/6

# 3.2 修改 添加删除元素
# 需求:1.在既有列表中,修改 jack ma为 father Ma 并在 开头 中间 末尾 分别添加 Yadong QI,zhangsan, LISI.
#      2.在以上完成修改添加后，执行：删除最后一名；删除名字叫 sicong Wang的；弹出最后一名，弹出第一名，并打印 第一名比第最后一名有钱字样。
# 方法：1.使用列表名[n]=直接赋值更改数据，采用列表名.append()在尾部增加，采用列表名.insert(n,XX)在任意位置增加，定点右移。
# 2.使用 /del 列表名[n]/执行删除已知位置；使用 /列表名.remove("XXX")/执行已知名字的删除；使用 /列表名.pop(n)/执行弹出后的值操作

Richmen = ["jack Ma", "Yanhong LI", "jianling WAng", "sicong WANg"]
print(Richmen)
Richmen[0]="father Ma"
print(Richmen)

Richmen.append("lisi")
print(Richmen)

Richmen.insert(0,"Yadong Qi")
print(Richmen)

Richmen.insert(2,"zhangsan")
print(Richmen)

# 注意：牢记表达式 Richmen[0]="father Ma"；Richmen.insert(0,"Yadong Qi")；Richmen.insert(2,"zhangsan")
# 插入有两种方式，实用性不同场景优势不同，新增用户还是需要排列用户

print("\n")
print(Richmen)

del Richmen[-1]  # 删除最后一名
print(Richmen)

Richmen.remove("sicong WANg")  # 删除 指定名字的信息
print(Richmen)


Richlast=Richmen.pop(-1)  # 弹出两个元素进行比较
print(Richmen)
Rich1st=Richmen.pop(0)
print("\n"+Rich1st.title()+"比"+Richlast.title()+"有钱!")

# tips：1.熟记表达式：知道位置的 知道名字的 剪切弹出还要用的.
#       2.remove只能删除第一个找到的，需要遍历之后检查循环删除