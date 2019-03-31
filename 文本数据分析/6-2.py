import re
import os
import glob
from collections import OrderedDict
def analysis(file):
    title=glob.glob('*.txt')#find every title with txt
    print(title)
    n={}
    w=[]
    for m in title:
        f=open(m,'r').read()
        f=re.findall(r'[a-zA-Z]+', f)#devide words
        for s in f:
            if s in w:
                n[s]+=1
            else:
                w.append(s)
                n[s]=1
        a = OrderedDict(sorted(n.items(), key=lambda x: x[1], reverse = True))#order the dict
        print(a)
        print("in %s the most frequent word is :" %m)
        for s in a:
            print(s+":  happen times is %d"%a[s])
            break
if __name__ == '__main__':
    file = '.'
    analysis(file)
        
                
            
    
    
