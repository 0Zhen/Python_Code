#pragma once

#define max_size 16

typedef struct {
    uint32_t buffer[max_size];
    uint8_t str;
    uint8_t end;
}circle_queue;

uint32_t Circle_Enqueue(uint32_t value, circle_queue* circle_queue_list);
uint32_t Circle_Dequeue(uint32_t* value, circle_queue* circle_queue_list);
uint32_t Circle_clear_queue(circle_queue* circle_queue_list);