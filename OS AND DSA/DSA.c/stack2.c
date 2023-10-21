=#include <stdio.h>
int max;
void push(int a[],int top,int x){
   if(top>=max-1){
        printf("OVERFLOW");
    }
    else{
        top=top+1;
        a[top]=x;
    }
}
void pop(int a[],int top){
    if(top==-1){
        printf("UNDERFLOW");
    }
    else{
        top=top-1;
    }
}
int main(){
    int top=-1;
    printf("ENTER THE MAXIMUM SIZE OF STACK: ");
    scanf("%d",&max);
    int a[max],x,ch;
    for(int i=0;i<100;i++){
    printf("ENTER 1 FOR INSERTING ELEMENT\n ENTER 2 FOR DELETING ELEMENT\n ENTER ANY OTHER FOR EXIT\n");
    scanf("%d",&ch);
    if(ch==1){
        printf("ENTER THE ELEMENT YOU WANT TO INSERT:");
        scanf("%d",&x);
        push(a,top,x);
        for(int j=0;j<top;j++){
            printf("%d",a[j]);
        }
    }
    else if(ch==2){
        pop(a,top);
         for(int j=0;j<top;j++){
            printf("%d",a[j]);
        }
    }
    else{
        break;
    }
    }
}

