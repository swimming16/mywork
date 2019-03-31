import os
import re

def count_num(a, b):
    shuzi = [0, 0, 0]
    path = os.path.join(a, b)
    f = open(path, 'r', encoding='UTF-8').readlines()
    print(f)
    for i in f:
        if re.match(r'^#', i) == None:                          
            pass
        else:
            shuzi[1] += 1                                                   #获得注释行数，只匹配单行注释
    if f[-1][-1:]=='\n':                                                     #最后一行为空行时
        shuzi[2] = f.count('\n')+1                                     #获得空行行数
        shuzi[0] = len(f)+1 - shuzi[2] - shuzi[1]                 #获得代码行数
    else:
        shuzi[2] = f.count('\n')
        shuzi[0] = len(f) - shuzi[2] - shuzi[1]
    return shuzi

def file_analysis(c, d):
    # for x in os.listdir(c):
    #     print(os.path.splitext(x))#splitext() devide file name and suffix name
    py = [x for x in os.listdir(c) if os.path.splitext(x)[1]==d]    #获得文件列表 list generator
    #print(py)
    the_num = [0, 0, 0]
    for i in py:
        num = count_num(c, i)
        the_num[0] += num[0]                #累计
        the_num[1] += num[1]
        the_num[2] += num[2]
    print('''统计得目录中：
             代码有 %s 行
             注释 %s 行
             空行 %s 行''' % (the_num[0], the_num[1], the_num[2]))

if __name__ == '__main__':
    file = '.'
    ext = '.py'
    file_analysis(file, ext)