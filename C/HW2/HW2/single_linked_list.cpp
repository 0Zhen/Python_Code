#include "single_linked_list.h"



uint32_t single_append(int new_data, single_node** head_ref)
{
    struct single_node* new_single_node = (struct single_node*)malloc(sizeof(struct single_node)); // 宣告一個位置給新的連結，這個位置大小等於single_node
    struct single_node* current = *head_ref; // 宣告一個指標指向(*head_ref)的位置

    new_single_node->value = new_data; // 把新的連結資料付值
    new_single_node->next = NULL; // 目前先將新的連結放在最後面


    /* 若這個傳進來的指標是空的，則代表沒有其他節點，因此新的連結就是他自己*/
    if ( (*head_ref) == NULL)
    {

        return RET_ERROR_EMPTY;
    }
    else
    {
        while (current->next != NULL) { // last->next == (*last).next
            current = current->next;
        }

        current->next = new_single_node;

    }



    return RET_SUCCESS;
}

uint32_t single_display(single_node** link)
{
    single_node* current = *link;

    while (current->next != NULL)
    {
        printf("%d -> ", current->value);
        current = current->next;
    };

    printf("%d -> \n", current->value);

    return RET_SUCCESS;
}

uint32_t single_ins(int before_target, int value, single_node** link)
{
    single_node* new_single_node = (struct single_node*)malloc(sizeof(struct single_node));
    single_node* current = *link;

    new_single_node->value = value;

    single_node* pre = new_single_node;

    if (current->value == before_target)
    {
        new_single_node->next = *link;
        *link = new_single_node;
        return RET_SUCCESS;
    }
    else
    {
        printf("current value = % d\n", current->value);
        while (current->value != before_target)
        {
            if (current->next == NULL)
            {
                return RET_ERROR_INVALID_DATA;
            }
            pre = current;
            current = current->next;
        }
        pre->next = new_single_node;
        new_single_node->next = current;


    }


    
    

    return RET_SUCCESS;
}

uint32_t single_del(int target, single_node** link)
{
    single_node* del_single_node = NULL;
    single_node* current = *link;
    single_node* pre = NULL;
    
    if (current->value == target)
    {
        *link = current->next;
        free(current);
        return RET_SUCCESS;
    }
    else
    {
       
        while (current->value != target)
        {
            if (current->next == NULL)
            {
                return RET_ERROR_INVALID_DATA;
            }
            pre = current;
            current = current->next;
        }

        pre->next = current->next;
        free(current);


    }



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    return RET_SUCCESS;
    

}