#include "doubly_linked_list.h"
uint32_t double_append(int new_data, double_node** head_ref)
{
	struct double_node* new_double_node = (struct double_node*)malloc(sizeof(struct double_node)); // �ŧi�@�Ӧ�m���s���s���A�o�Ӧ�m�j�p����double_node
	struct double_node* current = *head_ref; // �ŧi�@�ӫ��Ы��V(*head_ref)����m

    new_double_node->value = new_data; // ��s���s����ƥI��
    new_double_node->next = NULL; // �ثe���N�s���s����b�̫᭱
    new_double_node->pre = NULL;


    /* �Y�o�ӶǶi�Ӫ����ЬO�Ū��A�h�N��S����L�`�I�A�]���s���s���N�O�L�ۤv*/
    if ((*head_ref) == NULL)
    {

        return RET_ERROR_EMPTY;
    }
    else
    {
        while (current->next != NULL) { // last->next == (*last).next
            
            current = current->next;
            
        }

        current->next = new_double_node;
        new_double_node->pre = current;

    }



    return RET_SUCCESS;
}

uint32_t double_display(double_node** link)
{
    double_node* current = *link;

    while (current->next != NULL)
    {
        printf("%d -> ", current->value);
        current = current->next;
    };

    printf("%d -> \n", current->value);

    return RET_SUCCESS;
}

uint32_t double_prepend(int new_data, double_node** head_ref)
{
    struct double_node* new_double_node = (struct double_node*)malloc(sizeof(struct double_node)); // �ŧi�@�Ӧ�m���s���s���A�o�Ӧ�m�j�p����double_node
    struct double_node* current = *head_ref; // �ŧi�@�ӫ��Ы��V(*head_ref)����m

    new_double_node->value = new_data; // ��s���s����ƥI��
    new_double_node->next = NULL; // �ثe���N�s���s����b�̫᭱
    new_double_node->pre = NULL;


    /* �Y�o�ӶǶi�Ӫ����ЬO�Ū��A�h�N��S����L�`�I�A�]���s���s���N�O�L�ۤv*/
    if ((*head_ref) == NULL)
    {
        return RET_ERROR_EMPTY;
    }
    else
    {
        while (current->pre != NULL) { // last->next == (*last).next

            current = current->pre;

        }

        current->pre = new_double_node;
        new_double_node->next = current;
        *head_ref = new_double_node;

    }

    return RET_SUCCESS;

}


uint32_t double_ins(int before_target, int value, double_node** link)
{
    double_node* new_double_node = (struct double_node*)malloc(sizeof(struct double_node));
    double_node* current = *link;

    new_double_node->value = value;
    new_double_node->next = NULL;
    new_double_node->pre = NULL;

    double_node* pre{};



    if (current->value == before_target)
    {
        new_double_node->next = *link;
        *link = new_double_node;
        return RET_SUCCESS;
    }
    else
    {
        while (current->value != before_target)
        {
            if (current->next == NULL)
            {
                return RET_ERROR_INVALID_DATA;
            }
            current = current->next;
        }

        new_double_node->pre = current->pre;
        current->pre->next = new_double_node;
        new_double_node->next = current;
        current->pre = new_double_node;
        
    }

    return RET_SUCCESS;
}


uint32_t double_del(int target, double_node** link)
{
    double_node* del_double_node = NULL;
    double_node* current = *link;
    double_node* pre = NULL;

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
            
            current = current->next;
        }

        current->pre->next = current->next;
        current->next->pre = current->pre;
        free(current);


    }




    return RET_SUCCESS;

}