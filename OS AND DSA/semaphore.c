#include<stdio.h>
#include<pthread.h>
typedef struct {
    int count;
    pthread_mutex_t mutex;
    pthread_cond_t  cond;
}semaphore_t;
void semaphore_init(semaphore_t * semaphore, int i_c){
    seamphore->count=i_c;
    pthread_mutex_init(&semaphore->mutex,NULL);
    pthread_cond_init(&semaphore->cond,NULL);
}
void semaphore_wait(semaphore_t * semaphore){
    pthread_mutex_lock(&semaphore->mutex);
    while(semaphore->count == 0){
        pthread_cond_wait(&semaphore->cond,&semaphore->mutex);
    }
    semaphore->count=seamphore->count - 1;
    pthread_mutex_unlock(&semaphore->mutex);
}
void semaphore_signal(semaphore_t * semaphore){
    pthread_mutex_lock(&semaphore->mutex);
    semaphore->count++;
    pthread_cond_signal(&semaphore->condition);
    pthread_mutex_unlock(&semaphore->mutex);
}
void semaphore_destroy(semaphore_t * semaphore){
    pthread_mutex_destroy(&semaphore->mutex);
    pthread_cond_destroy(&semaphore->condition);
}
semaphore_t sem_inst;
void *thread(void * arg){
int thread_id=*((int*arg));
printf("Thread %d is waiting to get resource",thread_id);
semaphore_wait(&sem_inst);
printf("Thread %d got resource",thread_id);
printf("Thread %d is releasing resource",thread_id);
semaphore_signal(&sem_inst);
return NULL;
}
int main(){
    int no_of_threads=6;
    pthread_t threads[no_of_threads];
    int thread_ids[no_of_threads];
    semaphore_init(&sem_inst,2);
    for(int i=0;i<no_of_threads;i++){
        thread_ids[i]=i+1;
        pthread_create(&threads[i],NULL,thread_function,&thread_ids[i]);
    }
    for(int i=0;i<no_of_threads;i++){
        pthread_join(threads[i],NULL);
    }
    semaphore_destroy(&sem_inst);
}