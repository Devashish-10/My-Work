#include<stdio.h>
#include<stdlib.h>
int num=8,top=-1;
void push(int a[],int x){
    printf("%d  %d\n",top,x);
    if(top>=num-1){
        printf("STACK OVERFLOW");
    }
    else{
        top=top+1;
        
        a[top]=x;
    }
}
void pop(int a[]){
    if(top<=-1){
        printf("STACK UNDERFLOW");
}
else{
    top=top-1;
}
}
void display(int a[]){
    if(top>=0){
        for(int i=top;i>=(num-top);i++)
        {
            printf("%d",a[i]);
        }
    }
    else{
        printf("STACK IS EMPTY:");
    }
}
int main(){
    int ch,n,x;
    int a[8];
    while(ch!=0){
        printf("ENTER 1 TO PUSH AN ELEMENT  \n");
        printf("ENTER 2 TO PULL AN ELEMENT \n");
        printf("ENTER 0 TO EXIT \n");
        scanf("%d",&ch);
        if(ch==1){
            printf("ENTER ELEMENT TO BE ENTERED: ");
            scanf("%d",&x);
            push(a,x);
            display(a);
        }
        else if(ch==2){
            pop(a);
            display(a);
        }
        else{
            printf("ENTER A VALID OPTION");
            }
    }
   
}
