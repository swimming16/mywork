#pragma once
#include<stdio.h>
#include<time.h>
#include<conio.h>
#include<stdlib.h>
#include<Windows.h>
//变色
void B(char *);


//菜单
void Menu();


//贪吃蛇的地图
void Map();


//输出函数
void Show_map();


//蛇的结构
typedef struct _a{
	char x;
	char y;
	struct _a *next;
}Snake;


//创建蛇
void Create_snake(Snake *);


//食物的结构
typedef struct _b {
	char x;
	char y;
}Food;


//刷新食物
void Refresh_Food(Snake *);


//移动蛇
void Move_snake(Snake *);


//录入蛇
void Entry_snake(Snake *);


//判断蛇是否死亡，是否吃到了食物
void Judgment(char);


//给新长出来的身体定位
void Dw(char,Snake *);


//控制蛇
void Control_snake();


//初始化工作
void Initial();