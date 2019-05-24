#include "landownerV2.h"

landownerV2::landownerV2()
{
    //构造函数的作用就是初始化成员变量
    name="erdan";
    cout<<name;
    cout<<"默认构造函数被调用"<<endl;
    initCard();
}

landownerV2::landownerV2(string n,int s)
{
    name=n;
    score=s;
    initCard();
}
void landownerV2::showInof()
{
    cout<<name<<"的分数是"<<score<<endl;
}
void landownerV2::initCard()
{
    for(int i=0;i<54;i++)
    {
        postCard.push_back(i+1);
        remainCard.push_back(i+1);
    }
    playerCard.clear();
}
void landownerV2::showCard()
{
    for(auto i:postCard)
        cout<<i<<endl;
}
landownerV2::~landownerV2()
{
    //dtor
}
