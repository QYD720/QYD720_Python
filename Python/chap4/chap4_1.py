# Author : QYD720 
# Time : 2019/4/10

# 4.1 遍历列表
# 需求：遍历列表，并重复打印同样语意
# 方法：/for 暂存盒子 in 蓄水池 ：/代码实现遍历

Richmen = ["jack Ma", "yanhong LI", "ajianling WAng", "sicong WANg"]
for NB in Richmen:
    print(NB.upper()+" Father")
    print(NB.title()+"这么厉害，央行爸爸知道吗？\n")

print("央行：我不知道，Thanks")

# tips:代码结构，可以直接定义，不能忘记冒号；缩进是循环识别的方式，需要格外注意逻辑设计，报错固然可以发现，不报错也可以合法无逻辑 执行。
