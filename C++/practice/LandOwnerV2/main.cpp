#include <iostream>
#include"landownerV2.h"

using namespace std;

int main()
{
    //两种构造函数初始化的方式
    landownerV2 l("dan",90);
    l.showInof();

    /*
    //new相当于在堆内存里面取一块内存作为数据存储，不会占用宝贵的栈内存资源，new完记得delete释放内存！！！
    landownerV2* l2=new landownerV2();
    l2->showInof();
    delete l2;*/

    landownerV2* l3=new landownerV2();
    l3->showCard();
    return 0;
}
