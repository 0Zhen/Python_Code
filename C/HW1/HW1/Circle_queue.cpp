#pragma once

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Error.h"
#include "Circle_queue.h"

uint32_t Circle_Enqueue(uint32_t value, circle_queue* queue_list)
{

	if (queue_list->end == (queue_list->str ^ 16))
	{
		printf("\n--------full----------\n");

		return RET_ERROR_FULL;

	}
	else
	{
		printf("a = %d\n", ((queue_list->str + 1) & 0xF));
		queue_list->buffer[(queue_list->str & 0xF)] = value;
		queue_list->str++;


		for (int i = 0; i < max_size; i++)
		{
			printf("i = %d", i);
			printf("||%d||\n", queue_list->buffer[i]);
		}
	}




	printf("str = %d\n", queue_list->str);
	printf("end = %d\n", queue_list->end);
	printf("enqueue value =%d\n", value);
	return RET_SUCCESS;
}

uint32_t Circle_Dequeue(uint32_t* value, circle_queue* queue_list)
{
	if (queue_list->end == queue_list->str)
	{
		printf("\n--------Empty----------\n");
		return RET_ERROR_EMPTY;
	}
	else
	{
		*value = queue_list->buffer[((queue_list->end + 1) & 0xF)];
		queue_list->buffer[((queue_list->end) & 0xF)] = 0;
		queue_list->end++;

		for (int i = 0; i < max_size; i++)
		{
			printf("i = %d", i);
			printf("||%d||\n", queue_list->buffer[i]);
		}
		printf("str = %d\n", queue_list->str);
		printf("end = %d\n", queue_list->end);
		printf("-------------------------------------------------------\n");
	}
	return RET_SUCCESS;
}

uint32_t Circle_clear_queue(circle_queue* queue_list)
{
	uint32_t retval = RET_SUCCESS;
	memset(&queue_list->buffer, 0, sizeof(queue_list->buffer));
	printf("\n");

	queue_list->end = 0;
	queue_list->str = 0;

	for (int i = 0; i < max_size; i++)
	{
		printf("|%d| ", i);
		printf("%d\n", queue_list->buffer[i]);
	}
	return retval;
}