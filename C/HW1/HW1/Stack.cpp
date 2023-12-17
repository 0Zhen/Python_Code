#pragma once
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "Stack.h"
#include "Error.h"




uint32_t push(uint16_t value, stack* stack_list)
{
    uint32_t retval = RET_SUCCESS;

    if (stack_list->index < (max_size))
    {
        if (stack_list->index == 0)
        {
            stack_list->buffer[0] = value;
        }
        else
        {
            stack_list->buffer[(stack_list->index)] = value;
        }
        stack_list->index++;
        
    }
    else
    {
        printf("Buffer full\n");
        return RET_ERROR_FULL;
    }
    printf("\n");
    for (int i = 0; i < (sizeof(stack_list->buffer)) >> 2; i++)
    {
        printf("|%d| ", i);
        printf("%d\n", stack_list->buffer[i]);
    }
    return retval;
}

uint32_t pop(uint16_t* value, stack* stack_list)
{
    uint32_t retval = RET_SUCCESS;

    if (value == NULL)
    {
        return RET_ERROR_NULL;
    }
    if (stack_list->index == 0)
    {
        return RET_ERROR_EMPTY;
    }
    else
    {
        *value = (uint16_t)stack_list->buffer[(stack_list->index - 1)];
        stack_list->index--;
    }
    printf("\n");
    for (int i = 0; i < (sizeof(stack_list->buffer)) >> 2; i++)
    {
        printf("|%d| ", i);
        printf("%d\n", stack_list->buffer[i]);
    }
    return retval;
}

uint32_t clear(stack* stack_list)
{
    uint32_t retval = RET_SUCCESS;
    memset(&stack_list->buffer, 0, sizeof(stack_list->buffer));
    printf("\n");
    for (int i = 0; i < (sizeof(stack_list->buffer)) >> 2; i++)
    {
        printf("|%d| ", i);
        printf("%d\n", stack_list->buffer[i]);
    }
    return retval;
}