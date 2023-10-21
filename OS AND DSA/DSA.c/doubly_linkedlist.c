#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *lpt;
    struct node *rpt;
};
struct node *first;
void create(){
    char ch;
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    first=ptr;
    printf("ENTER A NUMBER IN LINKED LIST:");
    scanf("%d",&ptr->data);
    ptr->lpt=NULL;
    do{
       struct node *cpt=(struct node*)malloc(sizeof(struct node));
       printf("ENTER ANOTHER ELEMENT:\n");
       scanf("%d",&cpt->data);
       ptr->rpt=cpt;
       cpt->lpt=ptr;
       ptr=cpt;
       printf("DO YOU WANT MORE NODES:\n");
       scanf("%c",&ch);
        }
          while(ch=='Y');
          ptr->rpt=NULL;
         }
void traversal(struct node *p){
    while(p!=NULL){
        printf("ELEMENTS ARE %d\n:",p->data);
        p=p->rpt;
        }
}
void main(){
    create();
    traversal(first);
    }
         
     

    
