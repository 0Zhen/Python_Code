#include "four_way_linked_list.h"
#include "conio.h"

uint32_t four_way_append(int value, four_way_node** link)
{
	four_way_node* new_four_way_node = (struct four_way_node*)malloc(sizeof(struct four_way_node));
	four_way_node* current = *link;

    new_four_way_node->value = value; // 把新的連結資料付值
    new_four_way_node->next = NULL; // 目前先將新的連結放在最後面
    new_four_way_node->pre = NULL;
    new_four_way_node->down = NULL;
    new_four_way_node->up = NULL;


    /* 若這個傳進來的指標是空的，則代表沒有其他節點，因此新的連結就是他自己*/
    if ((*link) == NULL)
    {

        return RET_ERROR_EMPTY;
    }
    else
    {
        while (current->next != NULL) { // last->next == (*last).next

            current = current->next;

        }

        current->next = new_four_way_node;
        new_four_way_node->pre = current;

    }

    return RET_SUCCESS;
}


uint32_t four_way_prepend(int value, four_way_node** link)
{
    four_way_node* new_four_way_node = (struct four_way_node*)malloc(sizeof(struct four_way_node));
    four_way_node* current = *link;

    new_four_way_node->value = value; // 把新的連結資料付值
    new_four_way_node->next = NULL; // 目前先將新的連結放在最後面
    new_four_way_node->pre = NULL;
    new_four_way_node->down = NULL;
    new_four_way_node->up = NULL;

    /* 若這個傳進來的指標是空的，則代表沒有其他節點，因此新的連結就是他自己*/
    if ((*link) == NULL)
    {

        return RET_ERROR_EMPTY;
    }
    else
    {
        while (current->pre != NULL) { // last->next == (*last).next

            current = current->pre;

        }

        current->pre = new_four_way_node;
        new_four_way_node->next = current;
        *link = new_four_way_node;
    }

    return RET_SUCCESS;
}


uint32_t four_way_button(int value, four_way_node** link)
{
    four_way_node* new_four_way_node = (struct four_way_node*)malloc(sizeof(struct four_way_node));
    four_way_node* current = *link;

    new_four_way_node->value = value; // 把新的連結資料付值
    new_four_way_node->next = NULL; // 目前先將新的連結放在最後面
    new_four_way_node->pre = NULL;
    new_four_way_node->down = NULL;
    new_four_way_node->up = NULL;


    /* 若這個傳進來的指標是空的，則代表沒有其他節點，因此新的連結就是他自己*/
    if ((*link) == NULL)
    {

        return RET_ERROR_EMPTY;
    }
    else
    {
        while (current->down != NULL) { // last->next == (*last).next

            current = current->down;

        }

        current->down = new_four_way_node;
        new_four_way_node->up = current;

    }

    return RET_SUCCESS;
}


uint32_t four_way_display(four_way_node** link)
{
    four_way_node* current = *link;
    printf("start display\n");
    int ch;

    printf("head value = %d\n", current->value);
    while ((ch = _getch()) != 0x1B)
    {
        switch (ch)
        {
            case 72:
                printf("UP\n");
                if (current->up != NULL)
                {
                    printf("value = %d\n", current->up->value);
                    current = current->up;
                }
                else
                {
                    printf("Null\n");
                }
                break;
            case 80:
                printf("DOWN\n");
                if (current->down != NULL)
                {
                    printf("value = %d\n", current->down->value);
                    current = current->down;
                }
                else
                {
                    printf("Null\n");
                }
                break;
            case 75:
                printf("Left\n");
                if (current->pre != NULL)
                {
                    printf("value = %d\n", current->pre->value);
                    current = current->pre;
                }
                else
                {
                    printf("Null\n");
                }
                break;
            case 77:
                printf("Right\n");
                if (current->next != NULL)
                {
                    printf("value = %d\n", current->next->value);
                    current = current->next;
                }
                else
                {
                    printf("Null\n");
                }
                break;
            default:
                break;

        }
    }

    
    return RET_SUCCESS;
}