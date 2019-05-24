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
    for(auto i:remainCard)
        cout<<i<<endl;
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
    vector<int>::iterator iter =remainCard.begin();
    while(iter!=remainCard.end())
    {
        if(*iter==countCard)
            iter=remainCard.erase(iter);
        iter++;
    }
}
bool landownerV2::isContain(int m_countCard)
{
//    vector<int>::iterator iter =find(remainCard.begin(),remainCard.end(),m_countCard)
//    if(iter==remainCard.end())
//        return false;
//    else
//        return true;
      for (int i=0;i<remainCard.size() ;i++ )
      {
          if(m_countCard==remainCard[i])
            return true;
      }
      return false;
}
landownerV2::~landownerV2()
{
    //dtor
}
