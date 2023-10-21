#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *ptr;
};
struct node *top,*top1,*temp;
void create(){
    top=NULL;
}
void push(int x){
    if(top==NULL){
        top=(struct node*)malloc(sizeof(struct node));
        top->data=x;
        top->ptr=NULL;
    }
    else{
        temp=(struct node*)malloc(sizeof(struct node));
        temp->ptr=top;
        temp->data=x;
        top=temp;
       }
    }
void display(){
    top1=top;
    if(top1==NULL){
        printf("STACK IS EMPTY");
    }
    while(top1!=NULL){
        printf("%d\n",top1->data);
        top1=top1->ptr;
    }
}
void pop(){
    top1=top;
    if(top1==NULL){
        printf("STACK UNDERFLOW");
    }
    else{
        top=top1->ptr;
        free(top1);
      }
}
void main(){
  int ch,x;
  create();
  while(ch!=3){
  printf("ENTER 1 TO INSERT AN ELEMENT \n 2 TO DELETE AN ELEMENT \n 3 TO EXIT :\n");
  scanf("%d",&ch);
  if(ch==1){
   printf("ENTER AN ELEMENT TO INSERT: ");
   scanf("%d",&x);
   push(x);
   printf("ELEMENTS AFTER INSERTION ARE:\n");
   display();
  }
  else if(ch==2){
      pop();
      printf("ELEMENTS AFTER DELETION ARE:\n");
      display();
  }
  else{
      printf("ENTER A VALID CHIOCE:");
  }
  }
}

