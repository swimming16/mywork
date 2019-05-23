#include <iostream>
#include "FuncPtr.h"
using namespace std;


int main()
{
    int a[]={1,2,34,5};
    //show(a,4);
    int b[2][5]={{1,2,3,4,5},{10,6,7,8,9}};
    //show2(b,2);
    int c=3,d=4;
//    int (*powPtr)(int,int);//声明一个函数指针
//    powPtr=pow;//这个函数指针指向pow函数
    auto powPtr=pow;//使用auto自动识别函数指针类型，方便！！！auto同时必须初始化
    cout<<powPtr(c,d);

}
