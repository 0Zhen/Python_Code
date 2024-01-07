#pragma once
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Error.h"

struct double_node
{
	int value;
	struct double_node* pre;
	struct double_node* next;
};

uint32_t double_append(int value, double_node** link);
uint32_t double_prepend(int value, double_node** link);
uint32_t double_ins(int before_target, int value, double_node** link);
uint32_t double_del(int target, double_node** link);
uint32_t double_display(double_node** link);
#pragma once
