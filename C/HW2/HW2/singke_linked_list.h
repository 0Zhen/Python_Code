#pragma once
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Error.h"


uint32_t ins(void);
uint32_t del(void);
uint32_t mod(void);
uint32_t display(void);

struct node
{
	uint16_t id;
	struct node* next;
};