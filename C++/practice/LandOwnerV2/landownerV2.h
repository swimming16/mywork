#ifndef LANDOWNERV2_H
#define LANDOWNERV2_H

#include <string>
#include<iostream>
#include<vector>
using namespace std;

class landownerV2
{
    public:
        landownerV2();
        landownerV2(string,int);
        virtual ~landownerV2();

        void showInof();
        int Getscore() { return score; }
        void Setscore(int val) { score = val; }
        string Getname() { return name; }
        void Setname(string val) { name = val; }

        void touchCard(int );//摸牌的函数
        void initCard();
        void showCard();

    private:
        vector<int>postCard;//扑克牌总数
        vector<int>remainCard;//莫完后剩余的牌
        vector<int>playerCard;//玩家手中的牌
        int score;
        string name;
        int card[20];
};

#endif // LANDOWNERV2_H
