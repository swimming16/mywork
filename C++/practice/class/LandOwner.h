#ifndef LANDOWNER_H
#define LANDOWNER_H


class LandOwner
{
    private:
        int score;
        int card[20];
        string name;
    public:
        LandOwner();
        ~LandOwner();

        void TouchCard(int );//摸牌方法
        void showScore();//显示分数

    protected:

};

#endif // LANDOWNER_H
