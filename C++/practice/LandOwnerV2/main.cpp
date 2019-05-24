#include <iostream>
#include"landownerV2.h"

using namespace std;

int main()
{
    //两种构造函数初始化的方式
//    landownerV2 l("dan",90);
//    l.showInof();

    /*
    //new相当于在堆内存里面取一块内存作为数据存储，不会占用宝贵的栈内存资源，new完记得delete释放内存！！！
//    landownerV2* l2=new landownerV2();
//    l2->showInof();
//    delete l2;*/

//应用面向对象写程序
//    landownerV2* l3=new landownerV2();
//    l3->touchCard();
//    l3->showCard();
//    delete l3;

//应用this指针控制对象的变量和方法
//    landownerV2 *l4=new landownerV2();
//    l4->addScore(5);
//    l4->showInof();
//    l4->addScore(10);
//    l4->showInof();
//    l4->addScore(15);
//    delete(l4);

//应用this指针返回对象
    landownerV2 *l5=new landownerV2("狗子",80);
//    landownerV2 *l6=new landownerV2("石头",90);
//    l5->betterStu(*l6);//这里使用l6是指针，所以对象本身是*l6

    landownerV2 l6=landownerV2("石头",90);
    landownerV2 betterMan =l5->betterStu(l6);
    cout<<betterMan.Getname();

    return 0;
}
