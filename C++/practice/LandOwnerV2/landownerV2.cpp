#include "landownerV2.h"

landownerV2::landownerV2()
{
    //构造函数的作用就是初始化成员变量
    name="erdan";
    cout<<"默认构造函数被调用"<<endl;
    initCard();
    initScore();
}

landownerV2::landownerV2(string n,int s)
{
    name=n;
    score=s;
    initCard();
    initScore();
}
void landownerV2::initScore()
{
    this->scoreCount=1;
    this->Score=new double[scoreCount];
}
void landownerV2::addScore(double num)
{
    /*
    加入新的元素
    1.将新的元素加入数组score中
    2.创建一个新的指针和score指向地址一样，为了后面删除旧数组，避免野指针
    3.创建一个新数组newscore，大小为scoreCount+1
    4.数组大小+1
    5.将score数组中的元素复制到新数组中 memcpy
    6.newscore指向score的内容
    7.删除旧指针score
    */
    this->Score[this->scoreCount-1]=num;
    //cout<<Score[scoreCount-1]<<endl;
    double* ptr =Score;
    double* newScore =new double[scoreCount+1];
    scoreCount++;
    memcpy(newScore,Score,sizeof(double)*(scoreCount-1));
    Score=newScore;
    //cout<<newScore[scoreCount-2]<<endl;;
    delete ptr;
}
void landownerV2::showInof()
{
    //cout<<name<<"的分数是"<<score<<endl;
    cout<<"数组score的内容是:  ";
    for(int i=0;i<scoreCount-1;i++)
        cout<<Score[i]<<"  ";
    cout<<endl;
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
    for(auto i:remainCard)
    {
        cout<<i<<endl;
    }
}
void landownerV2::touchCard()
{
    int countCard;
    srand(time(NULL));
    countCard=rand()%54;//摸到的牌在0到53之间
    cout<<"摸到的牌是"<<countCard<<endl;
    if (isContain(countCard))//牌在剩余牌的里面
    {
        playerCard.push_back(countCard);
        DeleteCard(countCard);
    }
}
void landownerV2::DeleteCard(int countCard)
{
//    vector<int>::iterator iter =remainCard.begin();
//    while(iter!=remainCard.end())
//    {
//        if(*iter==countCard)
//            iter=remainCard.erase(iter);
//        iter++;
//    }

//  find函数包含头文件#include <algorithm>，比上面的写法简单
    auto iter =find(remainCard.begin(),remainCard.end(),countCard);
    if(iter!=remainCard.end())
    {
        iter=remainCard.erase(iter);//注意erase的是迭代器
    }
}
bool landownerV2::isContain(int m_countCard)
{
    vector<int>::iterator iter =find(remainCard.begin(),remainCard.end(),m_countCard);
    if(iter==remainCard.end())
        return false;
    else
        return true;

}

landownerV2& landownerV2::betterStu(landownerV2& other)
{
    /*注意->和.调用方法的方式
    如果是指针对象 如this指针则使用->来调用方法，如果直接是对象实例则使用.来调用方法
    */
    if(this->Getscore()>other.Getscore())//this是指针,other是对象实例
        return *this;//返回对象实例
    else
        return other;
}
landownerV2::~landownerV2()
{
    //dtor
}
