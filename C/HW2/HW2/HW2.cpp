// HW2.cpp : 此檔案包含 'main' 函式。程式會於該處開始執行及結束執行。
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Error.h"
#include "single_linked_list.h"
#include "doubly_linked_list.h"

int main()
{
    //single_node x;
    //x.value = 1;
    //x.next = NULL;
    //single_node* head_p = &x;
    //single_node** head_pp = &head_p;
    //


    //single_append(2, head_pp);
    //single_display(head_pp);
    //single_append(3, head_pp);
    //single_display(head_pp);
    //single_append(4, head_pp);
    //single_display(head_pp);
    //single_ins(2, 9, head_pp);
    //single_display(head_pp);
    //single_ins(1, 0, head_pp);
    //single_display(head_pp);
    //single_del(2, head_pp);
    //single_display(head_pp);
    //single_del(0, head_pp);
    //single_display(head_pp);

    double_node y;
    y.value = 0;
    y.pre = NULL;
    y.next = NULL;
    double_node* head_p = &y;
    double_node** head_pp = &head_p;

    double_append(1, head_pp);
    double_display(head_pp);
    double_append(2, head_pp);
    double_display(head_pp);
    double_prepend(3, head_pp);
    double_display(head_pp);
    double_prepend(5, head_pp);
    double_display(head_pp);
    double_ins(2, 7, head_pp);
    double_display(head_pp);
    double_ins(1, 8, head_pp);
    double_display(head_pp);
    double_del(5, head_pp);
    double_display(head_pp);
}

// 執行程式: Ctrl + F5 或 [偵錯] > [啟動但不偵錯] 功能表
// 偵錯程式: F5 或 [偵錯] > [啟動偵錯] 功能表

// 開始使用的提示: 
//   1. 使用 [方案總管] 視窗，新增/管理檔案
//   2. 使用 [Team Explorer] 視窗，連線到原始檔控制
//   3. 使用 [輸出] 視窗，參閱組建輸出與其他訊息
//   4. 使用 [錯誤清單] 視窗，檢視錯誤
//   5. 前往 [專案] > [新增項目]，建立新的程式碼檔案，或是前往 [專案] > [新增現有項目]，將現有程式碼檔案新增至專案
//   6. 之後要再次開啟此專案時，請前往 [檔案] > [開啟] > [專案]，然後選取 .sln 檔案
