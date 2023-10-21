#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};
struct node *front;
struct node *rear;
void insert(){
    struct node *p;
    int x;
    p=(struct node *)malloc(sizeof(struct node));
    if(p->next==NULL){
        printf("OVERFLOW");
    }
    else{
        printf("ENTER A NUMBER TO BE INSERTED:");
        scanf("%d",&x);
        p->data=x;
        if(front==NULL){
            front=p;
            rear=p;
            front->next=NULL;
            rear->next=NULL;
        }
        else{
            rear->next=p;
            rear=p;
            rear->next=NULL;
        }
    }
    }
void delete(){
    struct node *p;
    if(front==NULL){
        printf("UNDERFLOW");
    }
    else{
        p=front;
        front=front->next;
        free(p);
    } 
    
}
 void display(){
        struct node *p;
        p=front;
        if(front==NULL){
            printf("QUEUE IS EMPTY");
        }
        else{
            while(p!=NULL){
                printf("%d\n",p->data);
                p=p->next;
            }
        }
    }

void main(){
    int ch ;
    for(int i=0;i<20;i++){
        printf("ENTER 1 TO INSERT \n ENTER 2 TO DELETE \n PRESS ANYOTHER KEY TO EXIT");
        scanf("%d",&ch);
        if(ch==1){
            insert();
            display();
        }
        else if(ch==2){
            delete();
            display();
        }
        else{
            break;
        }
    }
}