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
    int n;
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    first=ptr;
    printf("ENTER A NUMBER IN LINKED LIST:");
    scanf("%d",&ptr->data);
    ptr->lpt=NULL;
    printf("ENTER HOW MANY MORE ELEMENTS DO YOU WANT:");
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
       struct node *cpt=(struct node*)malloc(sizeof(struct node));
       printf("ENTER ANOTHER ELEMENT:\n");
       scanf("%d",&cpt->data);
       ptr->rpt=cpt;
       cpt->lpt=ptr;
       ptr=cpt;
       if(cpt==NULL){
           ptr->rpt=NULL;}
    }
    }
void traversal(struct node *p){
    while(p!=NULL){
        printf("ELEMENTS ARE %d\n:",p->data);
        p=p->rpt;
        }
}
struct node *insertatstart(struct node *first,int data){
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    ptr->rpt=first;
    first->lpt=ptr;
    ptr->data=data;
    return ptr;
}
struct node *insertatend(struct node *first,int data){
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    struct node *p;
    p=first;
    ptr->data=data;
    while(p->rpt!=NULL){
        p=p->rpt;
     }
     p->rpt=ptr;
     ptr->lpt=p;
     ptr->rpt=NULL;
     return first;
}

struct node * insertatIndex(struct node *head, int data,int index){
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    struct node *p=first;
    printf("ELEMENTS AFTER INSERTION BETWEEN ARE:\n");
    int i =0;
    while(i!=index-1){
       p=p->rpt;
       i++;
    }
     ptr->data=data;
     ptr->rpt=p->rpt;
     p->rpt=ptr;
     return head;
}
struct node *deleteatbegining(struct node *first){
     struct node *ptr=first;
    first=first->rpt;
    free(ptr);
    return first;
}
struct node *deleteatend(struct node *first){
    struct node *p=first;
    struct node *q=p->rpt;
    while(q->rpt!=NULL){
        p=p->rpt;
        q=q->rpt;
    }
    p->rpt=NULL;
    free(q);
    return first;
}

struct node *deleteatindex(struct node *first,int index){
    struct node *p=first;
    struct node *q=first->rpt;
    for(int i=0;i<index-1;i++){
        p=p->rpt;
        q=q->rpt;
    }
    p->rpt=q->rpt;
    free(q);
    return first;
    }
    int main(){
    int data,index;
    create();
    traversal(first);
    printf("ENTER ELEMENT YOU WANT TO ENTER AT THE BEGINING:");
    scanf("%d",&data);
    first=insertatstart(first,data);
    printf("ELEMENTS AFTER INSERTION AT STARTING ARE:\n");
    traversal(first);
    printf("ENTER ELEMENT TO BE ENTERED AT THE END:");
    scanf("%d",&data);
    printf("ELEMENTS AFTER INSERTION AT END ARE:\n");
    first=insertatend(first,data);
    traversal(first);
    printf("ENTER THE INDEX WHERE YOU WANT TO INSERT THE ELEMENT:");
    scanf("%d",&index);
    printf("ENTER AN ELEMENT:");
    scanf("%d",&data);
    printf("ELEMENTS AFTER INSERTION IN INDEX ARE:");
    first=insertatIndex(first,data,index);
    traversal(first);
    printf("ELEMENT AFTER DELETION FROM BEGINING:");
    first=deleteatbegining(first);
    traversal(first);
    printf("ELEMENT AFTER DELETION FROM END:");
    first=deleteatend(first);
    traversal(first);
    printf("ENTER THE INDEX FROM WHERE YOU WANT TO REMOVE THE ELEMENT");
    scanf("%d",&index);
    printf("ELEMENT AFTER DELETION FROM GIVEN INDEX ARE:");
    first=deleteatindex(first,index);
    traversal(first);
    }
         
     

    
