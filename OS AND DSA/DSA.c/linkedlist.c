#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};
struct node *head;
void create(){
    char ch;
    int n;
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    head=ptr;
    printf("ENTER A NUMBER TO LINKED LIST:");
    scanf("%d",&ptr->data);
    printf("ENTER HOW MANY MORE NODES YOU WANT:");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        struct node *p=(struct node*)malloc(sizeof(struct node));
        printf("ENTER ANOTHER ELEMENT:");
        scanf("%d",&p->data);
        ptr->next=p;
        ptr=p;
        p=p->next;
        if(p==NULL){
            ptr->next=NULL;
        }
    }
}
void traversal(struct node *temp){
        while(temp->next!=NULL){
        printf("ELEMENTS ARE %d\n:",temp->data);
        temp=temp->next;
        }
}
struct node * insertatbegining(struct node *head, int data){
    printf("ELEMENTS AFTER INSERTION AT BEGINING:\n");
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    ptr->next=head;
    ptr->data=data;
    return ptr;

}
struct node * insertatIndex(struct node *head, int data,int index){
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    struct node *p=head;
    printf("ELEMENTS AFTER INSERTION BETWEEN ARE:\n");
    int i =0;
    while(i!=index-1){
       p=p->next;
       i++;
    }
     ptr->data=data;
     ptr->next=p->next;
     p->next=ptr;
     return head;
}
struct node * insertatend(struct node *head,int data){
     struct node *ptr=(struct node*)malloc(sizeof(struct node));
     struct node *p=head;
     ptr->data=data;
     printf("ELEMENTS AFTER INSERTION AT END:\n");
     while(p->next!=NULL){
     p=p->next;
     }
     p->next=ptr;
     ptr->next=NULL;
     return head;
}
struct node * deleteatbegining(struct node *head){
    struct node *ptr=head;
    head=head->next;
    free(ptr);
    return head;
}
struct node *deleteatend(struct node *head){
    struct node *p=head;
    struct node *q=p->next;
    while(q->next!=NULL){
        p=p->next;
        q=q->next;
    }
    p->next=NULL;
    free(q);
    return head;
}
struct node *deleteatindex(struct node *head,int index2){
    struct node *p=head;
    struct node *q=head->next;
    for(int i=0;i<index2-1;i++){
        p=p->next;
        q=q->next;
    }
    p->next=q->next;
    free(q);
    return head;
}
int main(){
    int x,x2,x3,index,index2;
    create();
    traversal(head);
    printf("ENTER A NUMBER TO INSERT:");
    scanf("%d",&x);
    head=insertatbegining(head,x);
    traversal(head);
    printf("ENTER AN INDEX WHERE YOU WANT TO INSERT THE NODE:\n");
    scanf("%d",&index);
    head=insertatIndex(head,  x,index);
    traversal(head);
    printf("ENTER A NUMBER TO BE INSERTED AT THE END:\n");
    scanf("%d",&x2);
    head=insertatend(head,x2);
    traversal(head);
    printf("ENTER A NUMBER TO BE DELETED FROM THE BEGINING:\n");
    scanf("%d",&x3);
    head=deleteatbegining(head);
    traversal(head);
    printf("ELEMENTS AFTER DELETION FROM END ARE\n");
    head=deleteatend(head);
    traversal(head);
    printf("ENTER AN INDEX FROM WHERE YOU WANT TO DELETE AN ELEMENT:\n");
    scanf("%d",&index2);
    head=deleteatindex(head,index2);
    traversal(head);
    return 0;
}


