#include <stdio.h>
#include <stdatomic.h>
typedef struct {
    _Atomic int lock;
}lock_and_wait_t;
void lock_and_wait_init(lock_and_wait_t* l){
    l->lock=0;
}
void lock(lock_and_wait_t* l){
    while(__sync_lock_test_and_set(&l->lock,1)){

    }
}
void unlock(lock_and_wait_t* l){
    l->lock=0;
}
lock_and_wait_t instances_of_lock_and_wait;
void * thread_function(void * arg){
    int thread_id=*((int*)arg);
    printf("Thread no %d waiting to get the thread\n",thread_id);
    lock(&instances_of_lock_and_wait);
    printf("Thread no %d got the thread ",thread_id);
    usleep(1000*1000);
    printf("Thread %d is releasing the lock",thread_id);
    unlock(&instances_of_lock_and_wait);
    return NULL;
}
int main(){
    int no_of_thread=6;
    pthread_t threads[no_of_thread];
    int thread_ids[no_of_thread];
    for(int i=0;i<no_of_thread;i++){
    thread_ids[i]=i+1;
    pthread_create(&threads[i],NULL,thread_function,&thread_ids[i]);
    for(int i=0;i<no_of_thread;i++){
        pthread_join(threads[i],NULL);
    }
    }
}




