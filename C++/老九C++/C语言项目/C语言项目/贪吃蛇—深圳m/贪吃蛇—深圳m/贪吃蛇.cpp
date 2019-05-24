#include"贪吃蛇.h"
#define N 30  //地图的宽
#define M 81  //地图的长
char map[N][M];//地图数组
int snake_length = 3;//蛇的长度
Snake *snake = (Snake *)malloc(sizeof(Snake));//初始化蛇结构的指针
Food food;  //定义食物的结构



			//菜单
void Menu()
{
	puts("-----------------------------------简单的说下规则wasd方向，ESC暂停，空格变颜色！----------------------------------------");
	Sleep(3000);
	system("cls");
	puts("----------------------------------------------- --还有3秒开始----------------------------------------------------");
	Sleep(1000);
	system("cls");
	puts("--------------------------------------------------还有2秒开始----------------------------------------------------");
	Sleep(1000);
	system("cls");
	puts("--------------------------------------------------还有1秒开始----------------------------------------------------");
	Sleep(1000);
	system("cls");
	puts("-----------------------------------------------------开始!-------------------------------------------------------");
}


//贪吃蛇的地图
void Map()
{
	int i, j;
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < M-1; j++)
		{
			if (i == 0 || i == N - 1 || j == 0 || j == M - 2)
				map[i][j] = '*';
			else
				map[i][j] = ' ';
		}
		map[i][j] = '\n';
	}
	map[i][j] = '\0';
}


//输出
void Show_map()
{
	system("cls");
		printf("%s", map);
	Sleep(100);
}


//创建蛇
void Create_snake(Snake *snake)
{
	snake->x = rand() % 78 + 1;
	snake->y = rand() % 26 + 1;
	char _x = snake->x;
	char _y = snake->y;
	while (--snake_length)
	{
		snake->next = (Snake *)malloc(sizeof(Snake));
		snake = snake->next;
		snake->x = _x;
		snake->y = ++_y;
	}
	snake->next = NULL;
}


//刷新食物
void Refresh_Food(Snake *snake)
{
p:	food.x = rand() % 78 + 1;
	food.y = rand() % 28 + 1;
	while (snake)
	{
		if (food.x == snake->x && food.y == snake->y)
			goto p;
		snake = snake->next;
	}
}


//移动蛇
void Move_snake(Snake *snake)
{
	static char  _x, _y, _x1, _y1;
	_x = snake->x;
    _y = snake->y;
	while (snake=snake->next)
	{
		_x1 = snake->x;
		_y1 = snake->y;
		snake->x = _x;
		snake->y = _y;
		_x = _x1;
		_y = _y1;
	}
}


//录入蛇与食物，并刷新地图
void Entry_snake(Snake *snake)
{
	Map();
	map[snake->y][snake->x] = '@';
	while (snake = snake->next)
		map[snake->y][snake->x] = '+';
	map[food.y][food.x] = '$';
}


//给新长出来的身子定位
void Dw(char c,Snake *_snake)
{
	char _x = _snake->x;
	char _y = _snake->y;
	_snake = _snake->next;
	if (c == 'w')
	{
		_snake->x = _x;
		_snake->y = ++_y;
	}
	else if(c=='s')
	{
		_snake->x = _x;
		_snake->y = --_y;
	}
	else if(c=='a')
	{
		_snake->x = ++_x;
		_snake->y = _y;
	}
	else
	{
		_snake->x = --_x;
		_snake->y = _y;
	}
	_snake->next = NULL;
}


//判断蛇是否死亡，是否吃到了食物
void Judgment(char c)
{
	Snake *_snake =snake;
	if (snake->x == food.x && snake->y == food.y)
	{
		while (_snake->next)
			_snake = _snake->next;
		_snake->next = (Snake *)malloc(sizeof(Snake));
		Dw(c, _snake);
		snake_length++;
		if (snake_length == (N-2)*(M-3))
		{
			fprintf(stderr, "恭喜你成功通过，你太牛了！！！");
			exit(EXIT_FAILURE);
		}
		Refresh_Food(snake);
		return;
	}


	if (snake->x == 0 || snake->x == 79 || snake->y == 0 || snake->y == 29)
	{
		fprintf(stderr, "墙都被你撞破了...,不说了修墙去了^&^");
		exit(EXIT_FAILURE);
	}
	while (_snake=_snake->next)
	{
		if (snake->x == _snake->x && snake->y == _snake->y)
		{
			fprintf(stderr, "你自己把自己撞死了...^&^");
			exit(EXIT_FAILURE);
		}
	}
}





//控制蛇
void Control_snake()
{
	char p = 0;
	char c, a = 'w';
z:	while (!kbhit());        //开始
	c = getch();
	if (c == 'w' || c == 'a' || c == 'd' || c == 's' || c == 27 || c == 32)
	{
		if (c == 27 || c == 32)
			goto s;
		else if ((c == 'w' && a == 's') || (c == 's' && a == 'w') || (c == 'a' && a == 'd') || (c == 'd' && a == 'a'))
			goto z;
		else
			a = c;
	}
	else
		goto z;
o:	Move_snake(snake);
s:	switch (c)
		{
			//上
		case 'w':
			snake->y--;
			break;
			//下
		case 's':
			snake->y++;
			break;
			//左
		case 'a':
			snake->x--;
			break;
			//右
		case 'd':
			snake->x++;
			break;
			//暂停
		case 27:
			goto z;
		case 32:
			B(&p);
			p++;
		}
	Judgment(c);
	Entry_snake(snake);
	Show_map();
	if (kbhit())
		c = getch();
	if (c == 'w' || c == 'a' || c == 'd' || c == 's' || c == 27 || c == 32)
	{
		if (c == 32 || c == 27)
			goto s;
		else if ((c == 'w' && a == 's') || (c == 's' && a == 'w') || (c == 'a' && a == 'd') || (c == 'd' && a == 'a'))
			c = a;
		else
			a = c;
	}
	else
		c = a;
	goto o;
}

//初始化工作
void Initial()
{
	Menu();
	Create_snake(snake);
	Refresh_Food(snake);
	Entry_snake(snake);
	Show_map();
}


//变色
void B(char *p)
{
	switch (*p)
	{
	case 0:system("color 0");
		break;
	case 1:system("color 1");
		break;
	case 2:system("color 2");
		break;
	case 3:system("color 3");
		break;
	case 4:system("color 4");
		break;
	case 5:system("color 5");
		break;
	case 6:system("color 6");
		break;
	case 7:system("color 7");
		break;
	case 8:system("color 8");
		break;
	case 9:system("color 9");
		break;
	case 10:system("color A");
		break;
	case 11:system("color B");
		break;
	case 12:system("color C");
		break;
	case 13:system("color D");
		break;
	case 14:system("color E");
		break;
	case 15:system("color F");
		break;
	default:
		*p = 0;
	}
}