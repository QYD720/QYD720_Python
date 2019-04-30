# Author : QYD720 
# Time : 2019/4/10
# 4.4 使用列表的一部分-列表切片
# 需求：
#       1.从已知列表里切出：前3名；中间随意3名；切到第8名；从5名切到结尾；切倒数2名均遍历打印出来。
#       2.通过切片复制前5名，上传到省级名单里
# 方法：列表名[:]


Rank = ["Jixuan Duan", "Qiwen He", "Mengyi Zha", "Bing Zheng", "Hequn Jin", "Siwei Chen", "Dingding", "Xiaozi Jia",
        "Luoxuan Jie", "Jiandan"]
print(len(Rank)) # 列表长度

Rank1_3 = Rank[0:3]
RankX_X3 = Rank[2:5]
Rank_8 = Rank[:8]
Rank5_ = Rank[5:]
Rank_X2 = Rank[-2:]
print()
print(Rank1_3, RankX_X3, Rank_8, Rank5_, Rank_X2, sep="\n")

# sep:string inserted between values, default a space.
# end:string appended after the last value, default a newline.

print

Provence = Rank[:5]

print(Provence)

