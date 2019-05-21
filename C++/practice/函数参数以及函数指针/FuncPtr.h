#ifndef FUNCPTR_H_INCLUDED
#define FUNCPTR_H_INCLUDED

using namespace std;


int pow(int num1,int num2);

int show(const int *value,int len)
{
    for (int i=0;i<len;i++)
    {
        cout<<value[i]<<endl;
    }
}
int show2(const int (*value)[5],int len)
    {
        for(int i=0;i<len;i++)
        {
            for(int j =0;j<5;j++)
                cout<<*(*(value+i)+j)<<endl;
        }
        return 0;
    }
int pow(int num1,int num2)
{
    int result=1;
    for(int i =0;i<num2;i++)
    {
        result*=num1;
    }
    return result;
}
#endif // FUNCPTR_H_INCLUDED
