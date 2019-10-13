import calendar
import datetime
class MyDate(object):
    def __init__(self):
        now_time = datetime.datetime.now()
        year = now_time.year
        month = now_time.month

        # 初始化
        self.result=[]
        # 当月总天数
        total_day = calendar.monthrange(year, month)[1]
        # 第一天
        first_day = datetime.date(year,month,1)
        # 第一天是周几
        first_week = first_day.weekday()    # 从0开始，0代表周一，6代表周日
        last_week = datetime.date(year,month,total_day).weekday()

        all_day = [x for x in range(1,total_day+1)]
        # 前面补充empty
        lines = []
        for i in range(first_week):
            lines.append('empty')
        for j in range(7-first_week):
            lines.append(all_day.pop(0))
        self.result.append(lines)

        while all_day:
            line = []
            for i in range(7):
                if len(line)<7 and all_day:
                    line.append(all_day.pop(0))
                else:
                    line.append('empty')
            self.result.append(line)

    def get_date(self):
        # 返回结果
        return self.result
    def print_date(self):
        # 将结果打印出来
        print(self.result)

if __name__ == '__main__':
    date = MyDate()
    date.print_date()