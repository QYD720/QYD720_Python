# 获取城市名对应的字符


mport requests
import re
import json
def main():
    # 12306 的城市名 和 城市名对应的代码 js 文件 url
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
    reponse = requests.get(url, verify=False)  # 关闭 https 证书的验证
    pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'  # 正则表达式，匹配城市名和城市代码
    result = re.findall(pattern, reponse.text)
    f = open('/Users/lec/Desktop/12306.json', 'w')  # 将字典保存在本地。
    datas = dict(result)
    json.dump(datas, f)
    f.close()


if __name__ == '__main__':
    main()


# 获取火车票信息并打印

import requests
import json
from prettytable import PrettyTable  # 使用这个库使我们的输出数据更加的美观


def get_train_url(text, data_dict):
    train = str(text).split(' ')  # 这里的 train 分别存储了 出发站，到达站，出发日期
    try:
        # 分别将城市转化为对应的城市代码
        from_station = data_dict[train[0]]
        to_station = data_dict[train[1]]
        date = train[2]
    except:
        date, from_station, to_station = '--', '--', '--'  # 出现无的情况，用 -- 代替
    # api url 的构造,也就是找到如上图所示的初始网站信息
    # https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-13&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT
    url = (
        'https://kyfw.12306.cn/otn/leftTicket/query?'
        'leftTicketDTO.train_date={}&'
        'leftTicketDTO.from_station={}&'
        'leftTicketDTO.to_station={}&'
        'purpose_codes=ADULT'
    ).format(date, from_station, to_station)
    print(url)
    return url


def get_train_data(url, code_dict):
    requests.packages.urllib3.disable_warnings()  # 关闭https证书验证警告
    tb = PrettyTable()  # 实例化一个对象
    tb.field_names = ["车次", "出发站", "目的地", "出发时间", "到达时间", "消耗时间", "一等座", "二等座", "软卧", "硬卧", "硬座", "无座"]  # 创造需要的字段
    try:
        r = requests.get(url, verify=False)  # 关闭 https 证书的验证
        raw_trains = r.json()['data']['result']  # 获取返回的json数据里的data部分的result结果
        for raw_train in raw_trains:  # 循环遍历每辆列车的信息
            train_list = []  # 一趟火车的全部信息
            data_list = raw_train.split('|')
            train_no = data_list[3]  # 车次号码
            train_list.append(train_no)
            from_station_code = data_list[6]  # 出发站
            from_station_name = code_dict[from_station_code]  # 将城市代码 替换成城市名字
            train_list.append(from_station_name)
            to_station_code = data_list[7]  # 终点站
            to_station_name = code_dict[to_station_code]  # 将城市代码 替换成城市名字
            train_list.append(to_station_name)
            start_time = data_list[8]  # 出发时间
            train_list.append(start_time)
            arrive_time = data_list[9]  # 到达时间
            train_list.append(arrive_time)
            lishi = data_list[10]  # 历时
            train_list.append(lishi)
            first_class_seat = data_list[31] or '--'  # 一等座
            train_list.append(first_class_seat)
            second_class_seat = data_list[30] or '--'  # 二等座
            train_list.append(second_class_seat)
            soft_sleep = data_list[23] or '--'  # 软卧
            train_list.append(soft_sleep)
            hard_sleep = data_list[28] or '--'  # 硬卧
            train_list.append(hard_sleep)
            hard_seat = data_list[29] or '--'  # 硬座
            train_list.append(hard_seat)
            no_seat = data_list[26] or '--'  # 无座
            train_list.append(no_seat)
            tb.add_row(train_list)  # 以补充行的形式来添加数据.

        print(tb)  # 打印查询结果
    except:
        print('输入信息有误，请重新输入')


def main():
    with open('/Users/lec/Desktop/12306.json', 'r') as f:
        data_dict = json.load(f)  # 城市名代码查询字典
        code_dict = {v: k for k, v in data_dict.items()}  # 将城市名和对应的城市名代码反转，形成新的字典。

    text = input("请输入出发地点，终点，日期\n")
    url = get_train_url(text, data_dict)  # 找到对应的 url
    get_train_data(url, code_dict)  # 信息处理函数


if __name__ == '__main__':
    main()

