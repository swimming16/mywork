#ifndef LANDOWNERV2_H
#define LANDOWNERV2_H


class landownerV2
{
    public:
        landownerV2();
        virtual ~landownerV2();

        int Getscore() { return score; }
        void Setscore(int val) { score = val; }
        string Getname() { return name; }
        void Setname(string val) { name = val; }
        int Getcard[20]() { return card[20]; }
        void Setcard[20](int val) { card[20] = val; }

    protected:

    private:
        int score;
        string name;
        int card[20];
};

#endif // LANDOWNERV2_H
