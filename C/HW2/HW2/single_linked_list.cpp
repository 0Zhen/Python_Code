#include "single_linked_list.h"



uint32_t ins(int new_data, node** head_ref )
{
    struct node* new_node = (struct node*)malloc(sizeof(struct node));
    struct node* last = *head_ref;

    new_node->value = new_data;
    new_node->next = NULL;

    if (*head_ref == NULL) {
        *head_ref = new_node;
        return RET_SUCCESS;
    }

    while (last->next != NULL) {
        last = last->next;
    }

    last->next = new_node;

    node* current = last;
    

    while (current != NULL) {
        printf("%d -> ", current->value);
        current = current->next;
    }

    return RET_SUCCESS;
}
