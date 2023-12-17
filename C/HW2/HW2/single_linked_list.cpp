#include "single_linked_list.h"



uint32_t ins(int new_data, node** head_ref )
{
    struct node* new_node = (struct node*)malloc(sizeof(struct node)); // 宣告一個位置給新的連結，這個位置大小等於node
    struct node* last = *head_ref; // 宣告一個指標指向(*head_ref)的位置

    new_node->value = new_data; // 把新的連結資料付值
    new_node->next = NULL; // 目前先將新的連結放在最後面

    /* 若這個傳進來的指標是空的，則代表沒有其他節點，因此新的連結就是他自己*/
    if (*head_ref == NULL) {
        *head_ref = new_node;
        return RET_SUCCESS;
    }

    while (last->next != NULL) { // last->next == (*last).next
        last = last->next;
    }

    last->next = new_node;

    node* current = *head_ref;
    

    do
    {
        printf("%d -> ", current->value);
        current = current->next;
    } while (current->next != NULL);
    printf("%d -> ", current->value);

    return RET_SUCCESS;
}
