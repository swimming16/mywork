#include "integer.h"
using namespace std;

integer::integer()
{
    num=0;
}
integer::integer(int value)
{
    num=value;
}
/*
1.integer& integer:: operator+(const integer& other) const
为什么不能这么写（integer&），因为sum是一个临时创建的对象，当离开这个函数时内存会被销毁，
所以当你返回sum引用对象时，sum本省已经被销毁不能使用
2.第一个const解读 const integer& other
表示other这个对象的内容不能被修改，只读内容
3.第二个const解读
表示不能修改自身的成员变量
*/

integer integer:: operator+(const integer& other) const
{
    integer sum(this->Getnum()+other.Getnum());
    sum.Setnum(this->Getnum()+other.Getnum());
    return sum;
}
integer::~integer()
{
    //dtor
}
