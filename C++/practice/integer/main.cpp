#include <iostream>
#include"integer.h"

using namespace std;

int main()
{
    integer i1(5),i2(2),i3(0);
    i3=i2+i1;//内部调用形式是i2.operator+(i1)
    cout<<i3.Getnum()<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
