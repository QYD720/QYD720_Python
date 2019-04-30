#Author : QYD720 
#Time : 2019/3/30

name='qI YAdonG AND HE jiaHonG'
print(name.title())
print(name.upper())
print(name.lower())

# name.函数 可以控制全大写 全小写 首字母大写
# 字符串就是'' ""里面的。


# 字符串的拼接
# 需求：输出 hello,XX!
# 字符串的拼接使用
first_name='YadoNG'
last_name='qi'
full_name=first_name+" "+last_name
print("Hello,"+full_name.title()+"!")

autohello="Hello,"+full_name.title()+"!"

print(autohello)

# 拼接+ 链接字符串，并使用.title修改后输出,也可以丢进字符串里批量化


# 制表符 换行符 替代word中的空格和Tab
# 输出 春晓
print('\t\t春晓\n\t穿棉不觉醒，\n\t处处蚊子咬。')
# \t=tab \n=enter

# 删除空白
# 需求：检查用户名重复，找出开头结尾误写的空白，确保无空白字符串
# 分析 strip函数的使用 lstrip切头 rstrip切尾 strip全切

sb_name=' wuxiaoming '
sb_name_l=sb_name.lstrip()
sb_name_r=sb_name.rstrip()
sb_name_ls=sb_name.strip()
print('l:'+sb_name_l+'\nr:'+sb_name_r+'\nls:'+sb_name_ls)

# \n制表符是string字符串的内容不能在括号之外
# strip的数据清洗作用


