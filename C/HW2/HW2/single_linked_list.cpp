#include "single_linked_list.h"



uint32_t append(int new_data, node** head_ref )
{
    struct node* new_node = (struct node*)malloc(sizeof(struct node)); // �ŧi�@�Ӧ�m���s���s���A�o�Ӧ�m�j�p����node
    struct node* last = *head_ref; // �ŧi�@�ӫ��Ы��V(*head_ref)����m

    new_node->value = new_data; // ��s���s����ƥI��
    new_node->next = NULL; // �ثe���N�s���s����b�̫᭱

    /* �Y�o�ӶǶi�Ӫ����ЬO�Ū��A�h�N��S����L�`�I�A�]���s���s���N�O�L�ۤv*/
    if (*head_ref == NULL) {
        *head_ref = new_node;
        return RET_SUCCESS;
    }

    while (last->next != NULL) { // last->next == (*last).next
        last = last->next;
    }

    last->next = new_node;


    return RET_SUCCESS;
}

uint32_t display(node link)
{
    node current = link;

    while (current.next != NULL)
    {
        printf("%d -> ", current.value);
        current = *current.next;
    };

    printf("%d -> \n", current.value);

    return RET_SUCCESS;
}

uint32_t ins(int before_target, int value, node** link)
{
    node* new_node = (struct node*)malloc(sizeof(struct node));
    node* last = *link;

    new_node->value = value;

    node* current = *link;
    node* pre = new_node;

    if (last->value == before_target)
    {
        new_node->next = last;
    }

    while (last->value != before_target)
    {
        pre = last;
        last = last->next;
    }
    pre->next = new_node;
    new_node->next = last;

    *link = pre;
    

    return RET_SUCCESS;
}

uint32_t del(int target, node** link)
{
    node* del_node = NULL;
    node* last = *link;
    node* head = NULL;

    if (last->value == target)
    {
        head = last;
        *last = *last->next;
        free(head);
        return RET_SUCCESS;
    }
    else
    {
        while (last->value != target)
        {
            if (last->next == NULL)
            {
                printf("No target");
                return RET_ERROR_INVALID_DATA;
            }
            del_node = last;
            last = last->next;
        }

        del_node->next = last->next;


        return RET_SUCCESS;
    }

}