#include <iostream>
#include"part1.h"

using namespace std;

函数模板和重载
函数模板适用于业务逻辑相似的函数，比如给不同类型的数组排序，本质上使用的排序方法都是一样的
而函数重载适用于业务逻辑不同的函数，比如同样吃东西，吃鸡蛋和吃米饭的操作就是不同的，此时使用函数重载更为合理


//void swap(int *p1,int *p2)
//{
//    int temp;
//    temp=*p1;
//    *p1=*p2;
//    *p2=temp;
//}
//void swap2(int &p1,int &p2)
//{
//    int temp;
//    temp=p1;
//    p1=p2;
//    p2=temp;
//}


template<typename T>//函数模板头，主要申明出一个参数的通用类型T！
void swap1(T &a,T &b)
{
    T temp;
    temp=a;
    a=b;
    b=temp;
}
int main()
{
    int num1=3,num2=5;
    string s1="zhang",s2="li";
    swap1(num1,num2);
    swap1(s1,s2);
    //swap2(num1,num2);
    cout<<num1<<num2;
    cout<<s1<<s2;
    return 0;
}
