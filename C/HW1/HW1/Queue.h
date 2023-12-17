
#define max_size 16

typedef struct {
    uint32_t buffer[max_size];
    uint8_t str;
    uint8_t end;
}queue;

uint32_t Enqueue(uint32_t value, queue* queue_list);
uint32_t Dequeue(uint32_t* value, queue* queue_list);
uint32_t clear_queue(queue* queue_list);