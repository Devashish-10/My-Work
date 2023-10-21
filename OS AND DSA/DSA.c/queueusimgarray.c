#include<stdio.h>
#include<stdlib.h>
int front=-1,rear=-1;
int queue[20];
void insert(int max){
    int x;
    printf("ENTER THE ELEMENTS:");
    scanf("%d",&x);
    if(rear==max-1){
        printf("OVERFLOW");
    }
    else if(front==-1&&rear==-1){
        front=0;
        rear=0;
        queue[rear]=x;
    }
    else{
        rear+=1;
        queue[rear]=x;
    }
    
}
void delete(int max){
    
    if(front==-1 || front>rear){
        printf("QUEUE IS EMPTY");
    }
    else{
        
        if(front==rear){
            front=-1;
            rear=-1;
        }
        else{
            front+=1;
        }
    }
}
void display(){
    for (int i=front;i<=rear;i++){
        printf("%d\n",queue[i]);
    }
}
void main(){
    int ch,max;
printf("ENTER MAXIMUM SIZE OF QUEUE:");
scanf("%d",&max);
    for(int i=0;i<20;i++){
    printf("ENTER 1 TO INSERT AN ELEMENT\n, 2 TO DELETE AN ELEMENT\n,AND ANY OTHER DIGIT TO EXIT\n");
    scanf("%d",&ch);
    if(ch==1){
    insert(max);
    printf("AFTER INSERTION OF ELEMENT QUEUE IS: \n");
    display();
    }
    else if(ch==2){
        delete(max);
        printf("AFTER DELETION OF ELEMENT QUEUE IS: \n");
        display();
    }
    else{
        break;
    }
    }
}