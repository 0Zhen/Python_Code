#include "four_way_linked_list.h"

uint32_t four_way_append(int value, four_way_node** link)
{
	four_way_node* new_four_way_node = (struct four_way_node*)malloc(sizeof(struct four_way_node));
	four_way_node* current = *link;

    new_four_way_node->value = value; // ��s���s����ƥI��
    new_four_way_node->next = NULL; // �ثe���N�s���s����b�̫᭱
    new_four_way_node->pre = NULL;


    /* �Y�o�ӶǶi�Ӫ����ЬO�Ū��A�h�N��S����L�`�I�A�]���s���s���N�O�L�ۤv*/
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