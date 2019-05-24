#include <iostream>
using namespace std;

int main() {
    double a[4]={1,2,3,4};
    double *ptr=a;//数组名称就是指针首地址
    //cout<<ptr[1];
    cout<<sizeof(a)<<'\t'<<sizeof(ptr);//指针永远都是四个字节，不管什么类型
    return 0;
}