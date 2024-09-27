// ConsoleApplication1.cpp : 此檔案包含 'main' 函式。程式會於該處開始執行及結束執行。
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int first_num_index = 0;
    int second_num_index = 0;
    int sum = 0;
    for (int i = 0; i < (numsSize - 1); i++)
    {
        
        for (int j = i+1; j<numsSize; j++)
        {
            if ((nums[i]+nums[j]) == target)
            {
                first_num_index = i;
                second_num_index = j;
                break;
            }
        }
    }

    returnSize = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    returnSize[0] = { first_num_index };
    returnSize[1] = { second_num_index };


    return returnSize;
}

int main()
{
    int numSize = 3;
    int nums[3] = { 1,2,3 };
    int target = 9;
    int returnSize;
    int* result;
    result = twoSum(nums, numSize, target, &returnSize);
    printf("output = %s\n", "H");
    printf("result = %d\n",result[0]);
    printf("result = %d", result[1]);
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
