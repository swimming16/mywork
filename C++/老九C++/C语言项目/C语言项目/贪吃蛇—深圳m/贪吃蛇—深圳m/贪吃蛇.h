#pragma once
#include<stdio.h>
#include<time.h>
#include<conio.h>
#include<stdlib.h>
#include<Windows.h>
//��ɫ
void B(char *);


//�˵�
void Menu();


//̰���ߵĵ�ͼ
void Map();


//�������
void Show_map();


//�ߵĽṹ
typedef struct _a{
	char x;
	char y;
	struct _a *next;
}Snake;


//������
void Create_snake(Snake *);


//ʳ��Ľṹ
typedef struct _b {
	char x;
	char y;
}Food;


//ˢ��ʳ��
void Refresh_Food(Snake *);


//�ƶ���
void Move_snake(Snake *);


//¼����
void Entry_snake(Snake *);


//�ж����Ƿ��������Ƿ�Ե���ʳ��
void Judgment(char);


//���³����������嶨λ
void Dw(char,Snake *);


//������
void Control_snake();


//��ʼ������
void Initial();