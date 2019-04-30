#Author : QYD720 
#Time : 2019/4/

# 3.1 列表是什么？
# 需求：从列表中提取第二个元素
# 实现：[,,]列表，调用列表名[n]，来实现，并可以加用.title upper lower来实现数据清洗

Richmen = ["jack Ma", "Yanhong LI", "jianling WAng", "sicong WANg"]

Rich1st= Richmen[0]

print("中国首富是"+Rich1st.upper()+"!")
print("最后一名是"+Richmen[-1].lower()+".")


# 注意：逗号隔开，元素性质要知道是字符串还是数字；
# 从0开始而不是1开始，所以首富应该是0索引；
# [-1,-2]等代表倒数第一倒数第二;注意指定序列[]不是括号

