#ifndef LANDOWNERV2_H
#define LANDOWNERV2_H

#include <algorithm>
#include <cstring>
#include<iostream>
#include<vector>
#include<cstdlib>
#include<ctime>
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

        void touchCard();//摸牌的函数
        void initCard();
        void showCard();
        bool isContain(int);//判断摸得牌是否在剩余牌中
        void DeleteCard(int);//从剩余的牌中删除摸到的手牌
        void initScore();
        void addScore(double);//在数组score中加入新的元素！！！动态的一个一个的向数组中加入元素
        landownerV2& betterStu(landownerV2&);

    private:
        vector<int>postCard;//扑克牌总数
        vector<int>remainCard;//莫完后剩余的牌
        vector<int>playerCard;//玩家手中的牌
        int score;//分数
        int scoreCount;//score数组元素数组个数
        double* Score;//使用指针指向一个score数组
        string name;
        int card[20];
};

#endif // LANDOWNERV2_H
