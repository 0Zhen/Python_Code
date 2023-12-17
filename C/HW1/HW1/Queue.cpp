#pragma once

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Error.h"
#include "Queue.h"

uint32_t Enqueue(uint32_t value, queue* queue_list)
{
	
	if (queue_list->str >=16)
	{
		printf("\n--------full----------\n");
		
		return RET_ERROR_FULL;
		
	}
	else
	{
		printf("str = %d\n", queue_list->str);
		queue_list->buffer[queue_list->str] = value;
		queue_list->str++;
		printf("str = %d\n", queue_list->str);

		for (int i = 0; i < sizeof(queue_list->buffer) >> 2; i++)
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

uint32_t Dequeue(uint32_t* value, queue* queue_list)
{
	if (queue_list->str == 0)
	{
		printf("\n--------Empty----------\n");
		return RET_ERROR_EMPTY;
	}
	else
	{
		printf("str = %d\n", queue_list->str);
		*value = queue_list->buffer[0];
		for (int i = 0; i < max_size-1; i++)
		{
			queue_list->buffer[i] = queue_list->buffer[i + 1];
			printf("i = %d", i);
			printf("str = %d\n", queue_list->str);
		}
		queue_list->buffer[max_size - 1] = 0;
		printf("str = %d\n", queue_list->str);
		queue_list->str--;

		for (int i = 0; i < max_size - 1; i++)
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

uint32_t clear_queue(queue* queue_list)
{
	uint32_t retval = RET_SUCCESS;
	memset(&queue_list->buffer, 0, sizeof(queue_list->buffer));
	printf("\n");

	queue_list->end = 0;
	queue_list->str = 0;

	for (int i = 0; i < (sizeof(queue_list->buffer)) >> 2; i++)
	{
		printf("|%d| ", i);
		printf("%d\n", queue_list->buffer[i]);
	}
	return retval;
}