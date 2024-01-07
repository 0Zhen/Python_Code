#pragma once
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Error.h"

struct single_node
{
	int value;
	struct single_node* next;
};
   
uint32_t single_append(int value, single_node** link);
uint32_t single_ins(int before_target, int value, single_node** link);
uint32_t single_del(int target, single_node** link);
uint32_t single_display(single_node** link);

