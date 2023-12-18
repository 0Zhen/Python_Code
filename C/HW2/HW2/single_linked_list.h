#pragma once
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Error.h"

struct node
{
	int value;
	struct node* next;
};
   
uint32_t append(int value, node** link);
uint32_t ins(int before_target, int value, node** link);
uint32_t del(int target, node** link);
uint32_t mod(void);
uint32_t display(node link);

