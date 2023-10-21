#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};
void traversal(struct node *ptr){
    while(ptr!=0){
        printf("ELEMENTS ARE %d\n",ptr->data);
        ptr=ptr->next;
    }
    }
    void main(){
        struct node*first;
        struct node*second;
        struct node *third;
        struct node *fourth;
        first=(struct node*)malloc(sizeof(struct node));
        second=(struct node*)malloc(sizeof(struct node));
        third=(struct node*)malloc(sizeof(struct node));
        fourth=(struct node*)malloc(sizeof(struct node));
        first->data=67;
        first->next=second;
        second->data=44;
        second->next=third;
        third->data=78;
        third->next=fourth;
        fourth->data=104;
        fourth->next=NULL;
        traversal(first);
    }
    