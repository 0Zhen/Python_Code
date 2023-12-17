#include <iostream>
#include <stdio.h>
#include "Error.h"
#include "Queue.h"







uint32_t push(uint16_t value, stack* stack_list)
{
    uint32_t retval = RET_SUCCESS;
    if (stack_list->index < (max_size - 1))
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
        return retval;
    }
    else
    {
        printf("Buffer full\n");
        return RET_FULL;
    }

    return retval;
}

uint32_t pop(uint16_t* value, stack* stack_list)
{
    uint32_t retval = RET_SUCCESS;

    if (value == NULL)
    {
        return RET_ERROR;
    }
    if (stack_list->index == 0)
    {
        return RET_EMPTY;
    }
    else
    {
        *value = (uint16_t)stack_list->buffer[(stack_list->index - 1)];
        stack_list->index--;
    }
    return retval;
}