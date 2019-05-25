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

integer integer:: operator+(integer other)
{
    integer sum(this->num+other.num);
    sum.Setnum(this->Getnum()+other.Getnum());
    return sum;
}
integer::~integer()
{
    //dtor
}
