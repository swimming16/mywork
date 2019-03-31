import os
import re
import glob
import numpy as np

def analyze(path):
    num=[0,0,0]
    sum=[0,0,0]
    num=np.array(num)
    sum=np.array(sum)
    a=glob.glob('*.py')
    for m in a:
        f=open(m,'r',encoding='UTF-8').readlines()
        if f[-1]=='\n':
            num[0]=f.count('\n')+1
        for i in f:
            if re.match(r'^#', i) == None:                          
                pass
            else:
                num[1] += 1   
        num[2]=len(f)-num[0]-num[1]
        sum+=num
    print(sum)

if __name__ == '__main__':
    file = '.'
    analyze(file)