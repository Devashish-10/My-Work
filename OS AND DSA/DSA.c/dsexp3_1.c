#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};
void traversal(struct node *ptr){
    while(ptr!=NULL){
        printf("ELEMENTS ARE %d\n",ptr->data);
        ptr=ptr->next;
    }
    }
struct node * insertatbegining(struct node *first, int data){
    printf("ELEMENTS AFTER INSERTION AT BEGINING:\n");
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    ptr->next=first;
    ptr->data=data;
    return ptr;

}
struct node * insertatIndex(struct node *first, int data,int index){
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    struct node *p=first;
    printf("ELEMENTS AFTER INSERTION BETWEEN ARE:\n");
    int i =0;
    while(i!=index-1){
       p=p->next;
       i++;
    }
     
     ptr->data=data;
     ptr->next=p->next;
     p->next=ptr;
     return first;
}
struct node * insertatend(struct node *first,int data){
     struct node *ptr=(struct node*)malloc(sizeof(struct node));
     struct node *p=first;
     ptr->data=data;
     printf("ELEMENTS AFTER INSERTION AT END:\n");
     while(p->next!=NULL){
     p=p->next;
     }
     p->next=ptr;
     ptr->next=NULL;
     return first;
}
void main(){
        int x,index;
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
        printf("ENTER A NUMBER TO INSERT:");
        scanf("%d",&x);
        first=insertatbegining(first,x);
        traversal(first);
        printf("ENTER AN INDEX WHERE YOU WANT TO INSERT THE NODE:");
        scanf("%d",&index);
        first=insertatIndex(first,  x,index);
        traversal(first);
        first=insertatend(first,x);
        traversal(first);

    }
    