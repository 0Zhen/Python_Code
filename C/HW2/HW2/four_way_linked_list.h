#pragma once
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Error.h"

struct four_way_node
{
	int value;
	struct four_way_node* pre;
	struct four_way_node* next;
	struct four_way_node* up;
	struct four_way_node* down;
};

uint32_t four_way_append(int value, four_way_node** link);
uint32_t four_way_prepend(int value, four_way_node** link);
uint32_t four_way_top(int value, four_way_node** link);
uint32_t four_way_button(int value, four_way_node** link);
//uint32_t four_way_ins(int before_target, int value, four_way_node** link);
uint32_t four_way_del(int target, four_way_node** link);
uint32_t four_way_display(four_way_node** link);
