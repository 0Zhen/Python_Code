// HW1.cpp : 此檔案包含 'main' 函式。程式會於該處開始執行及結束執行。
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Stack.h"
#include "Queue.h"
#include "Error.h"
#include "Circle_queue.h"

stack stack_list_real;
stack* stack_list = &stack_list_real;

queue queue_list_real;
queue* queue_list = &queue_list_real;

circle_queue circle_queue_list_real;
circle_queue* circle_queue_list = &circle_queue_list_real;
typedef char str[80];

int main()
{
	while (true)
	{
		char option;
		str cmd = {  };
		printf("\n");
		printf("||=============== ChrisLee's HW1 : ===============||\n");
		printf("|| Type : int,  MAX_LENG : 16                     ||\n");
		printf("|| CMD : 1 = stack, 2 = queue, 3 = circle queue   ||\n");
		printf("|| Quit = 'quit'                                  ||\n");
		printf("||================================================||\n\n");
		option = getchar();
		while (getchar() != '\n');

		switch (option)
		{
			case '1':
				while (true)
				{
					printf("\n");
					printf("||=============== ChrisLee's Stack : ===============||\n");
					printf("|| Type : int,  MAX_LENG : 16                       ||\n");
					printf("|| CMD : push <value>, pop, clear, list, quit       ||\n");
					printf("||==================================================||\n\n");

					printf("Input CMD : ");


					scanf_s("%s", &cmd, 10);

					if (strcmp("quit", cmd) == 0)
					{
						printf(">> Quit.");
						break;
					} // if
					else if (strcmp("push", cmd) == 0)
					{
						printf("> Input push value (int) : ");
						int value = 0;
						int get = 0;
						get = scanf_s("%d", &value);

						while (get != 1)
						{
							printf("\n> Error input type, try again (int) : ");
							while (getchar() != '\n');
							get = scanf_s("%d", &value);
						} // while
						push(value, stack_list);

					} // else if
					else if (strcmp("pop", cmd) == 0)
					{

						uint16_t value = 0;
						if (pop(&value, stack_list) == RET_ERROR_EMPTY)
						{
							printf("Stack is empty\n");
						}
						else if (pop(&value, stack_list) == RET_ERROR_FULL)
						{
							printf("Stack is full\n");
						}
						else
						{
							printf("> Output pop value (int) : %d", value);
						}

					} // else if
					else if (strcmp("clear", cmd) == 0)
					{

						uint16_t value = 0;
						if (clear(stack_list) == RET_SUCCESS)
						{
							printf("Stack is empty\n");
						}
						else if (pop(&value, stack_list) == RET_ERROR_FULL)
						{
							printf("Stack is full\n");
						}
						else
						{
							printf("> Output pop value (int) : %d", value);
						}


					} // else if
					else
					{
						printf(">> \"%s\" is not a correct CMD. \n", cmd);
					} // else

				} // while

				break;

			case '2':
				while (true)
				{
					printf("\n");
					printf("||=============== ChrisLee's Circle Queue : ========||\n");
					printf("|| Type : int,  MAX_LENG : 16                       ||\n");
					printf("|| CMD : enqueue <value>  , clear, dequeue, quit    ||\n");
					printf("||==================================================||\n\n");

					printf("Input CMD : ");


					scanf_s("%s", &cmd, 10);

					if (strcmp("quit", cmd) == 0)
					{
						printf(">> Quit.");
						break;
					} // if
					else if (strcmp("enqueue", cmd) == 0)
					{
						printf("> Input push value (int) : \n");
						int value = 0;
						int get = 0;
						get = scanf_s("%d", &value);

						while (get != 1)
						{
							printf("\n> Error input type, try again (int) : ");
							while (getchar() != '\n');
							get = scanf_s("%d", &value);
						} // while
						Enqueue(value, queue_list);

					} // else if
					else if (strcmp("dequeue", cmd) == 0)
					{
						uint32_t value = 0;
						uint32_t ret = Dequeue(&value, queue_list);
						if (ret == RET_ERROR_EMPTY)
						{
							printf("Stack is empty\n");
						}
						else if (ret == RET_ERROR_FULL)
						{
							printf("Stack is full\n");
						}
						else
						{
							printf("> Output dequeue value (int) : %d", value);
						}

					} // else if
					else if (strcmp("clear", cmd) == 0)
					{
						clear_queue(queue_list);

					} // else if
				}

				break;

			case '3':
				while (true)
				{
					printf("\n");
					printf("||=============== ChrisLee's Circle Queue : ========||\n");
					printf("|| Type : int,  MAX_LENG : 16                       ||\n");
					printf("|| CMD : enqueue <value>  , clear, dequeue, quit    ||\n");
					printf("||==================================================||\n\n");

					printf("Input CMD : ");


					scanf_s("%s", &cmd, 10);

					if (strcmp("quit", cmd) == 0)
					{
						printf(">> Quit.");
						break;
					} // if
					else if (strcmp("enqueue", cmd) == 0)
					{
						printf("> Input push value (int) : ");
						int value = 0;
						int get = 0;
						get = scanf_s("%d", &value);

						while (get != 1)
						{
							printf("\n> Error input type, try again (int) : ");
							while (getchar() != '\n');
							get = scanf_s("%d", &value);
						} // while
						Circle_Enqueue(value, circle_queue_list);

					} // else if
					else if (strcmp("dequeue", cmd) == 0)
					{
						uint32_t value = 0;
						uint32_t ret = Circle_Dequeue(&value, circle_queue_list);
						if (ret == RET_ERROR_EMPTY)
						{
							printf("Stack is empty\n");
						}
						else if (ret == RET_ERROR_FULL)
						{
							printf("Stack is full\n");
						}
						else
						{
							printf("> Output pop value (int) : %d", value);
						}

					} // else if
					else if (strcmp("clear", cmd) == 0)
					{
						Circle_clear_queue(circle_queue_list);

					} // else if
				}

				break;

			default:
				
				break;


		}




		
		
	}
	return 0;
} // main

// 執行程式: Ctrl + F5 或 [偵錯] > [啟動但不偵錯] 功能表
// 偵錯程式: F5 或 [偵錯] > [啟動偵錯] 功能表

// 開始使用的提示: 
//   1. 使用 [方案總管] 視窗，新增/管理檔案
//   2. 使用 [Team Explorer] 視窗，連線到原始檔控制
//   3. 使用 [輸出] 視窗，參閱組建輸出與其他訊息
//   4. 使用 [錯誤清單] 視窗，檢視錯誤
//   5. 前往 [專案] > [新增項目]，建立新的程式碼檔案，或是前往 [專案] > [新增現有項目]，將現有程式碼檔案新增至專案
//   6. 之後要再次開啟此專案時，請前往 [檔案] > [開啟] > [專案]，然後選取 .sln 檔案
