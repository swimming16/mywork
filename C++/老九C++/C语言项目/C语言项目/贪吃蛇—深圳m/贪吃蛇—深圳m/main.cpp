#include"贪吃蛇.h"

int main()
{
	srand(time(NULL));         //给随机种子
	Initial();                 //初始化工作
	Control_snake();
	return 0;
}