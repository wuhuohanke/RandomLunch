#coding=utf-8
from random import choice
lunchList = ['灵芝妹子米线', 'Mc', 'KFC', '小吴家家', '大盘鸡', '大一统烤肉', '定食屋', '百年石锅', '姜元烤肉', '必胜客',
             '哆啦A梦', '八方云集', '冬日恋歌', '一韩亭', '小花卷', '黄焖鸡', '15号楼食堂', '亚惠', '西北马记牛肉面',
             '软景中心探索', '老汤肉酱拉面', '肉蟹煲', '品利源']
f = open('D:\PycharmProjects\RandomLunch\LunchHistory.txt', encoding='utf8')
lines = f.readlines()
f.close()
newLines = []
for line in lines:
    line = line.rstrip()
    newLines.append(line)
new_list = []
if len(newLines) == 0:
    new_list = lunchList
elif len(newLines) == len(lunchList):
    fClear = open('D:\PycharmProjects\RandomLunch\LunchHistory.txt', 'w')
    fClear.truncate()
    fClear.close()
    new_list = lunchList
else:
    for lunch in lunchList:
        if lunch not in newLines:
            new_list.append(lunch)
choiceToday = choice(new_list)
print('\n' + 'Please find recommended lunch for today as below:' + '\n' + '------------------------------------' + '\n')
print(choiceToday)
f2 = open('D:\PycharmProjects\RandomLunch\LunchHistory.txt', 'a', encoding='utf8')
f2.write(str(choiceToday) + '\n')
f2.close()
