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

uint32_t ins(int value, node** link);
uint32_t del(void);
uint32_t mod(void);
uint32_t display(void);

