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
Ϊʲô������ôд��integer&������Ϊsum��һ����ʱ�����Ķ��󣬵��뿪�������ʱ�ڴ�ᱻ���٣�
���Ե��㷵��sum���ö���ʱ��sum��ʡ�Ѿ������ٲ���ʹ��
2.��һ��const��� const integer& other
��ʾother�����������ݲ��ܱ��޸ģ�ֻ������
3.�ڶ���const���
��ʾ�����޸�����ĳ�Ա����
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
