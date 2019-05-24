#include <iostream>

using namespace std;

int sum(int a,int b)
{
    return a+b;
}
void input(int value[],int len)
{
    for(int i=0;i<5;i++)
    {
        cin>>value[i];
    }
}
int main()
{

    int value[]={};
    input(value,5);
    cout<<value[4];

}
