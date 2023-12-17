
#define max_size 16

typedef struct {
    uint32_t buffer[max_size];
    uint8_t index;
}stack;

uint32_t push(uint16_t value, stack* stack_list);
uint32_t pop(uint16_t* value, stack* stack_list);


