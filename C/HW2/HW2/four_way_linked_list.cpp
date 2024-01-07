#include "four_way_linked_list.h"

uint32_t four_way_append(int value, four_way_node** link)
{
	four_way_node* new_four_way_node = (struct four_way_node*)malloc(sizeof(struct four_way_node));
	four_way_node* current = *link;

    new_four_way_node->value = value; // 把新的連結資料付值
    new_four_way_node->next = NULL; // 目前先將新的連結放在最後面
    new_four_way_node->pre = NULL;


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