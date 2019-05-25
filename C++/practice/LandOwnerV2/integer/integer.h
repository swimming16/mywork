#ifndef INTEGER_H
#define INTEGER_H
#include<iostream>
using namespace std;

class integer
{
    public:
        integer();
        integer(int);
        virtual ~integer();

        int Getnum() { return num; }
        void Setnum(int val) { num = val; }
        integer operator+(integer);//重载加号运算符，将operator+理解成一个add函数即可

    protected:

    private:
        int num;
};

#endif // INTEGER_H
