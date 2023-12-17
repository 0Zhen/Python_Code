// ConsoleApplication1.cpp : 此檔案包含 'main' 函式。程式會於該處開始執行及結束執行。
//

#include <iostream>
#include <stdio.h>
#define max_size 16
#define RET_SUCCESS 1
#define RET_FULL 2
#define RET_ERROR 3
#define RET_EMPTY 4

typedef struct {
    uint32_t buffer[max_size];
    uint8_t index;
}stack;

stack stack_list_real;
stack* stack_list = &stack_list_real;

uint32_t push(uint16_t value)
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

uint32_t pop(uint16_t* value)
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
        *value = (uint16_t) stack_list->buffer[(stack_list->index - 1)];
        stack_list->index--;
    }

}



int main()
{
    uint16_t value = 0;
    for (int i = 0; i < 5; i++)
    {
        push(10+i);
        printf("push%d\n", 10 + i);

        for (int i = 0; i < max_size; i++)
        {
            printf("%d ", stack_list->buffer[i]);
        }
        printf("\n");
    }
    
    for (int i = 0; i < 5; i++)
    {
        pop(&value);
        printf("pop = %d\n", value);

        for (int i = 0; i < max_size; i++)
        {
            printf("%d ", stack_list->buffer[i]);
        }
        printf("\n");
    }

    for (int i = 0; i < 5; i++)
    {
        push(9);
        printf("push%d\n", 9);

        for (int i = 0; i < max_size; i++)
        {
            printf("%d ", stack_list->buffer[i]);
        }
        printf("\n");
    }
    //pop(&value);
    //printf("%d\n", stack_list->buffer[0]);

    //printf("Value =%d\n", value);
    //printf("%d\n", stack_list->buffer[0]);

    //printf("%x\n", cal_crc32(&buf, 32, init));
}

