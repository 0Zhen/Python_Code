#include "single_linked_list.h"



uint32_t ins(int new_data, node** head_ref )
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

    node* current = *head_ref;
    

    do
    {
        printf("%d -> ", current->value);
        current = current->next;
    } while (current->next != NULL);
    printf("%d -> ", current->value);

    return RET_SUCCESS;
}
